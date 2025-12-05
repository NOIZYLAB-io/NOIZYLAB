def register_incident(type: str, user: str, notes: str):
    return {
        "reported": True,
        "type": type,
        "user": user,
        "notes": notes
    }


def request_assist_service():
    return {"dispatch": True, "eta": "3 minutes"}

