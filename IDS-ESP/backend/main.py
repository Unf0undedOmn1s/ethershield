from fastapi import FastAPI
from sqlmodel import SQLModel, Field, Session, create_engine
from typing import Optional
from datetime import datetime
import hashlib

# ---------- Database Setup ----------

DATABASE_URL = "postgresql://audituser:securepass@localhost/rogue_audit"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    return Session(engine)

# ---------- Model Definition ----------

class RogueAccessPoint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    ssid: str
    mac_address: str
    vendor: Optional[str]
    timestamp: datetime
    hash: str

# ---------- FastAPI ----------

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/log/")
def log_rogue_ap(ssid: str, mac_address: str, vendor: str = ""):
    timestamp = datetime.utcnow()
    data_to_hash = f"{ssid}|{mac_address}|{vendor}|{timestamp.isoformat()}"
    hashed = hashlib.sha256(data_to_hash.encode()).hexdigest()

    rogue_ap = RogueAccessPoint(
        ssid=ssid,
        mac_address=mac_address,
        vendor=vendor,
        timestamp=timestamp,
        hash=hashed
    )

    with get_session() as session:
        session.add(rogue_ap)
        session.commit()

    return {
        "status": "logged",
        "ssid": ssid,
        "mac_address": mac_address,
        "hash": hashed,
        "timestamp": timestamp.isoformat()
    }