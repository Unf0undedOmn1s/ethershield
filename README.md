## EtherShield by Whiteguard
*For detailed progress check at ethershield/ethershield-main/docs/ethershield-report.md*

# Problem
- Phishing campaigns have become more sophisticated, often mimicking real services (e.g., banks, email providers) with high visual and linguistic accuracy.
- Phishers use rapidly changing domains and IP addresses to evade detection.
- Attackers customize phishing emails using public or leaked information to target specific individuals or organizations.
- SMS phishing (smishing) and mobile-friendly spoof pages trick users who can’t inspect URLs easily.
- Many phishing incidents go unreported or are scattered across platforms.

# Solution
- Use real-time visual similarity detection, maintain up-to-date threat intelligence feeds to identify cloned pages quickly.
- Employ live DNS lookup + cache with TTL monitoring.
- Cross-reference WHOIS data and certificate transparency logs.
- Use heuristics based on domain age, registrar reputation, and hosting location.
- Monitor for targeted wording and context using NLP (natural language processing).
- Enable users to report suspicious messages, creating feedback loops, provide anomaly detection on inbound communication patterns.


# Timeline: 8 Months (Can be adjustable)
# Month 1 - Tasks:
- Define threat model and scope phishing detection.
- Decide on features: DNS Blacklist, Heuristics, Web Scraping, Threat Intelligence.
- Choose on tech stack (language, framework, database, API)

## Roles
- Team Lead (Project Leader): Ensures objectives are clearly defined and timelines set - Gkarsoudis Dimitrios.
- Security Analyst: Maps phishing attack vectors to detection logic - Grivas Marios, Kalantzis Ektoras.
- Backend Developer: Prepares software architecture and data flow plans - Gkarsoudis Dimitrios (AWS), Grivas Marios, Mpetas Alexandros.
- Frontend Developer: Proposes dashboard and user interface layout - Grivas Marios, Kalantzis Ektoras.

# Month 2 - Backend Setup:
- Build FastAPI/Flask server skeleton.
- Setup MongoDB/PostgreSQL.
- Design database schema for phishing logs.

# Month 3 - Core Logic Implemetantion:
- Implement phishing detection (suspicious URLs, known patterns)
- Integrate DNS Blacklisting.

# Month 4 - Frontend Development: 
- Build dashboard (React, or other frontend framework).
- Implement visualization of logs, feedback submission.

# Month 5 - Testing and Feedback:
- Perform unit testing, integration testing.
- Validate blacklist lookups and phishing report accuracy.

# Month 6 - Finalization and Deployment (2 spare months for improvement):
- Polish UI and detection precision.
- Deploy backend to cloud (AWS, Firebase).
- Prepare documentation, README and pitch materials.

# Copyright (c) 2025 Whiteguard 
# Meet the team of Whiteguard:
- Grivas Marios **Offensive Security Practicioner**
- Gkarsoudis N. Dimitrios **IoT & Hardware**
- Kalantzis E. Ektoras **Offensive Security Practicioner**
- Mpetas Alexandros **IoT & Hardware**
# This software is the intellectual property of Whiteguard.
# For more, read EULA at ethershield/EULA.
