import json
import os
from datetime import datetime

LOG_FILE = "logs/conversations.json"
LEADS_FILE = "logs/leads.json"
UNKNOWN_QUESTIONS_FILE = "logs/unknown_questions.json"


def _load_file(filepath: str) -> dict:
    if not os.path.exists(filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            json.dump({}, f)
        return {}
    with open(filepath) as f:
        try:
            data = json.load(f)
            return data if isinstance(data, dict) else {}
        except json.JSONDecodeError:
            return {}


def _save_file(filepath: str, data: dict) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def log_lead(name: str, email: str, notes: str) -> None:
    data = _load_file(LEADS_FILE)
    date_key = datetime.now().strftime("%Y-%m-%d")
    data.setdefault(date_key, []).append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "name": name,
        "email": email,
        "notes": notes,
    })
    _save_file(LEADS_FILE, data)


def log_unknown_question(question: str) -> None:
    data = _load_file(UNKNOWN_QUESTIONS_FILE)
    date_key = datetime.now().strftime("%Y-%m-%d")
    data.setdefault(date_key, []).append({
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "question": question,
    })
    _save_file(UNKNOWN_QUESTIONS_FILE, data)


def _load() -> dict:
    return _load_file(LOG_FILE)


def _save(data: dict) -> None:
    _save_file(LOG_FILE, data)


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
