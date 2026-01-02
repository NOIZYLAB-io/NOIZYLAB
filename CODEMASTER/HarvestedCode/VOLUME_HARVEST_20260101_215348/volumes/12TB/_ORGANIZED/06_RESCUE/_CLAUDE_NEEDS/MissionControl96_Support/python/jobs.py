from apscheduler.schedulers.background import BackgroundScheduler
from ..auto.firmware import check_and_stage
from ..auto.policy import PolicyEngine

engine = PolicyEngine()

def start_scheduler(app):
    sched = BackgroundScheduler()
    sched.add_job(check_and_stage, "cron", hour=3, minute=0)
    sched.add_job(lambda: engine.evaluate(), "interval", seconds=30)
    sched.start()
