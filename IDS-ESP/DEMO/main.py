from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import hashlib
import os

app = FastAPI()

scans = []

class ScanData(BaseModel):
    ssid: str
    bssid: str
    zone: str

@app.post("/submit-scan")
def submit_scan(data: ScanData):
    combined = f"{data.ssid}-{data.bssid}-{data.zone}"
    hash = hashlib.sha256(combined.encode()).hexdigest()
    scan_entry = {"ssid": data.ssid, "bssid": data.bssid, "zone": data.zone, "hash": hash}
    scans.append(scan_entry)
    return {"hash": hash}

@app.get("/scans")
def get_scans():
    return JSONResponse(scans)

# Serve static files (including index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")