from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
import json, os

app = FastAPI()

class Event(BaseModel):
    user_id: str
    session_id: str
    event_name: str
    consent: bool = Field(default=False)
    ts: float | None = None

@app.post("/collect")
def collect(evt: Event):
    if not evt.consent:
        return {"ok": True, "dropped": True}
    rec = evt.dict()
    rec["server_ts"] = datetime.utcnow().isoformat()
    os.makedirs("data/landing", exist_ok=True)
    with open("data/landing/events.ndjson", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    return {"ok": True}
