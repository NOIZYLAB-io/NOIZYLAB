import schedule, time
from noizy_cockpit_orchestrator import trigger_ritual

schedule.every().sunday.at("21:00").do(lambda: trigger_ritual("build_capsule"))
schedule.every().day.at("09:00").do(lambda: trigger_ritual("activate_sequoia"))

while True:
    schedule.run_pending()
    time.sleep(60)
