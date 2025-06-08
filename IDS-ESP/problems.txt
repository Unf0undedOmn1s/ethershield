# Problem 1:
- To block ICMP flood connections at the system level, Python IDS can only detect and alert. Blocking must be done by configuring your system firewall (e.g., Windows Firewall or iptables on Linux).
- *Solution*: Automatic call a system command to block offending IPs when a flood is detected. Example: Blocking IP on Windows - Subprocess in Python to adda a Firewall Rule.
