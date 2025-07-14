# filepath: /home/marios-g/Desktop/ethershield-main/IDS-ESP/static/phishing_api.py
from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import urlparse

app = FastAPI()

class URLRequest(BaseModel):
    url: str

@app.post("/check-phishing")
def check_phishing(data: URLRequest):
    url = data.url.lower()
    parsed = urlparse(url)
    hostname = parsed.hostname
    if not hostname:
        return {"result": "invalid"}
    if "login" in url or "verify" in url:
        return {"result": "phishing"}
    return {"result": "safe"}