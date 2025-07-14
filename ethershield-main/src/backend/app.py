from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scapy.all import sniff, IP, ICMP, TCP
import threading
import time
from threading import Lock
import subprocess

def block_ip_windows(ip):
    rule_name = f"Block_ICMP_{ip}"
    cmd = [
        "netsh", "advfirewall", "firewall", "add", "rule",
        f"name={rule_name}", "dir=in", "action=block", f"remoteip={ip}"
    ]
    subprocess.run(cmd, capture_output=True)

threats_lock = Lock()
traffic_lock = Lock()
stats_lock = Lock()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

threats = []
traffic = []
blocked_ips = set()
stats = {
    "threats_blocked": 0,
    "active_connections": 0,
    "traffic_events": 0,
    "data_processed": 0,
    "events_per_minute": 0,
    "cpu": 0,
    "memory": 0,
    "storage": 0,
    "blocked_ips": []
}

ip_packet_count = {}
ip_port_count = {}
last_minute_events = []
icmp_times = {}

ICMP_FLOOD_THRESHOLD = 50
DDOS_ACTIVE_THRESHOLD = 3

def packet_callback(packet):
    now = time.strftime("%H:%M:%S")
    with stats_lock:
        stats["traffic_events"] += 1
    last_minute_events.append(time.time())

    if IP in packet:
        src = packet[IP].src
        ip_packet_count[src] = ip_packet_count.get(src, 0) + 1

        if ICMP in packet and packet[ICMP].type == 8:
            t = time.time()
            icmp_times.setdefault(src, []).append(t)
            icmp_times[src] = [x for x in icmp_times[src] if t - x < 10]

            if len(icmp_times[src]) > ICMP_FLOOD_THRESHOLD and src not in blocked_ips:
                block_ip_windows(src)
                blocked_ips.add(src)
                with stats_lock:
                    stats["threats_blocked"] += 1
                    stats["blocked_ips"] = list(blocked_ips)
                with threats_lock:
                    threats.insert(0, {
                        "message": f"ICMP flood detected and blocked from {src}",
                        "level": "critical",
                        "time": now
                    })
                    threats[:] = threats[:20]

            ddos_ips = sum(1 for times in icmp_times.values() if len(times) > ICMP_FLOOD_THRESHOLD)
            if ddos_ips >= DDOS_ACTIVE_THRESHOLD:
                with threats_lock:
                    threats.insert(0, {
                        "message": f"DDoS attack active: {ddos_ips} sources flooding ICMP",
                        "level": "critical",
                        "time": now
                    })
                    threats[:] = threats[:20]

            with threats_lock:
                threats.insert(0, {
                    "message": f"ICMP Ping from {src}",
                    "level": "info",
                    "time": now
                })
                threats[:] = threats[:20]

        if TCP in packet:
            dport = packet[TCP].dport
            ip_port_count.setdefault(src, set()).add(dport)
            if len(ip_port_count[src]) > 10:
                with threats_lock:
                    threats.insert(0, {
                        "message": f"Port scan detected from {src}",
                        "level": "warning",
                        "time": now
                    })
                    threats[:] = threats[:20]

        if ip_packet_count[src] > 100:
            with threats_lock:
                threats.insert(0, {
                    "message": f"Possible DDoS from {src}",
                    "level": "critical",
                    "time": now
                })
                threats[:] = threats[:20]

    if IP in packet:
        desc = ""
        if TCP in packet:
            desc = f"TCP {packet[IP].src}:{packet[TCP].sport} → {packet[IP].dst}:{packet[TCP].dport}"
        elif ICMP in packet:
            desc = f"ICMP {packet[IP].src} → {packet[IP].dst}"
        else:
            desc = f"IP {packet[IP].src} → {packet[IP].dst}"
        with traffic_lock:
            traffic.insert(0, {"event": desc, "time": now})
            traffic[:] = traffic[:20]

def packet_sniffer():
    sniff(prn=packet_callback, store=0)

def stats_updater():
    while True:
        cutoff = time.time() - 60
        while last_minute_events and last_minute_events[-1] < cutoff:
            last_minute_events.pop()
        with stats_lock:
            stats["events_per_minute"] = len(last_minute_events)
            stats["cpu"] = 30
            stats["memory"] = 40
            stats["storage"] = 50
            stats["active_connections"] = len(ip_packet_count)
            stats["data_processed"] = round(stats["traffic_events"] * 0.5, 2)
        time.sleep(2)

@app.on_event("startup")
def start_sniffer():
    threading.Thread(target=packet_sniffer, daemon=True).start()
    threading.Thread(target=stats_updater, daemon=True).start()

@app.get("/stats")
def get_stats():
    with stats_lock:
        return stats

@app.get("/threats")
def get_threats():
    with threats_lock:
        return threats

@app.get("/traffic")
def get_traffic():
    with traffic_lock:
        return traffic
