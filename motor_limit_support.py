def motor_predict(intention: str):
    if "fix" in intention:
        return "AUTO_RUN_REPAIR"
    if "help" in intention:
        return "OPEN_SUPPORT"
    return "READ_OUT"

