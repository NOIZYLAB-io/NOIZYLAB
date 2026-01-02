def narrate(event):
    action = event["action"]; dev = event["device_id"]; ts = event["ts"]
    return f"At {ts}, {action} ritual on {dev}."
