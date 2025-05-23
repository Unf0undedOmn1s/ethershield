from sqlmode import SQLModel, Field
from typing import Optional
from datetime import datetime

class RogueAccessPoint(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True):
    ssid: str
    mac_address: str
    vendor: Optional[str]
    timestamp: datetime
    hash: str
