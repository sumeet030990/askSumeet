import json
import os
from datetime import datetime

LOG_FILE = "logs/conversations.json"


def _load() -> dict:
    if not os.path.exists(LOG_FILE):
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "w") as f:
            json.dump({}, f)
        return {}
    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def _save(data: dict) -> None:
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)


def log_session_start(session_id: str, user_profile: dict) -> None:
    data = _load()
    date_key = datetime.now().strftime("%Y-%m-%d")
    data.setdefault(date_key, {})[session_id] = {
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "last_active": datetime.now().isoformat(timespec="seconds"),
        "user": {
            "name": user_profile.get("name", ""),
            "email": user_profile.get("email", ""),
            "phone": user_profile.get("phone", ""),
        },
        "messages": [],
    }
    _save(data)


def log_message(session_id: str, message: dict) -> None:
    data = _load()
    # Find which date this session belongs to
    for _, sessions in data.items():
        if session_id in sessions:
            sessions[session_id]["messages"].append(message)
            sessions[session_id]["last_active"] = datetime.now().isoformat(timespec="seconds")
            _save(data)
            return
