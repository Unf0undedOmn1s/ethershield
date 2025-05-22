import requests
import random

ssids = ["UOI Open", "Kilykeio AP", "Fake Kilykeio AP", "Fake UOI Open"]
zones = ["Building A", "Library", "Cafeteria"]

def simulate():
    for _ in range(3):
        data = {
            "ssid": random.choice(ssids),
            "bssid": f"AA:BB:{random.randint(0,99):02}:CC:{random.randint(0,99):02}:DD",
            "zone": random.choice(zones)
        }
        res = requests.post("http://localhost:8000/submit-scan", json=data)
        print(res.json())

if __name__ == "__main__":
    simulate()