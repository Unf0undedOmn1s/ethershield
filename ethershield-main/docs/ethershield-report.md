
# Ethershield – Project Report

_Last updated: 14 July 2025_

## Accomplishments

### Branding and Online Presence
- Designed Ethershield visual identity (logo, brand colors, fonts)
- Created a public landing website with product details and a demo request form
- Launched Instagram, YouTube, and X pages
- Published phishing awareness content and interactive quizzes on social media
- Created online Google Form -> *https://docs.google.com/forms/d/e/1FAIpQLSdTCLXHSaL_LRmX59-HVZN97Ml4gtby_Kog35wV7wUZpQNVWg/viewform?usp=header*

### Backend & Dashboard Development
- Implemented FastAPI backend for:
  - Threat logging
  - Network traffic monitoring
  - Basic DDoS pattern recognition
- JavaScript-powered frontend dashboard with real-time metrics
- Live updating of:
  - Threats Blocked
  - Active Connections
  - Events per Minute
  - Resource Usage (CPU, RAM, Disk)
- Display of real-time traffic logs and system status

### Phishing Detection
- Phishing feature design: User submits a suspicious link
- Comparing URLs against a large database of phishing patterns
- Output shows whether the link is malicious or clean
- Currently building model integration using XGBoost (planned)

### Documentation & Strategy
- Created pitch deck presentation based on Blueground/OpenCoffee Athens format - 12/07/2025
- Defined MVP roadmap in MVP-Framework.md - 02/07/2025
- Documented assumptions, questions & answers, and mentorship notes - 28/06/2025
- Added LICENSE (custom EULA) and README - 14/07/2025

## Testing & Deployment
- Hosted dashboard and API locally
- Simulated hping3 traffic for DDoS detection validation
- Domain registered (whiteguard.org)
- Email routing configured via Improvmx (info@whiteguard.org → Gmail)

## Business Development
- Secured 3rd place in university Ideathon competition
- Participated in Piraeus Startup Accelerator
- Conducted mentor sessions (Mentor: Fanis Sklavnitis-Piraeus Bank | Date: 01/07/2025)
- Filled out business model, vision, and funding plan

## Next Steps
- Integrate phishing detection model (XGBoost)
- Harden backend security and deploy on AWS
- Make “Request a Demo” form send email via SMTP (Gmail + FastAPI)
- Make app/.exe (Downloadable-Flutter iOS/Android)
- Beta test with SMEs and freelancers
- Seek seed funding / grants (The Ask: €50,000)
