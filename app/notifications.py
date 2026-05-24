import os
import urllib.request
import urllib.parse


def send_message_notification(session_id: str, user_profile: dict, message: str) -> None:
    token = os.environ.get("PUSHOVER_TOKEN")
    user = os.environ.get("PUSHOVER_USER")
    if not token or not user:
        return

    name = user_profile.get("name") or "Anonymous"

    payload = urllib.parse.urlencode({
        "token": token,
        "user": user,
        "title": f"AskSumeet — Message from {name}",
        "message": f"{message}\n\nSession: {session_id}",
    }).encode()

    try:
        req = urllib.request.Request("https://api.pushover.net/1/messages.json", data=payload)
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass


def send_session_notification(session_id: str, user_profile: dict) -> None:
    token = os.environ.get("PUSHOVER_TOKEN")
    user = os.environ.get("PUSHOVER_USER")
    if not token or not user:
        return

    name = user_profile.get("name") or "Anonymous"
    email = user_profile.get("email") or "—"
    phone = user_profile.get("phone") or "—"

    message = f"New session started\nName: {name}\nEmail: {email}\nPhone: {phone}\nSession: {session_id}"

    payload = urllib.parse.urlencode({
        "token": token,
        "user": user,
        "title": "AskSumeet — New Visitor",
        "message": message,
    }).encode()

    try:
        req = urllib.request.Request("https://api.pushover.net/1/messages.json", data=payload)
        urllib.request.urlopen(req, timeout=5)
    except Exception:
        pass
