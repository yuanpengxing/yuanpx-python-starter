# -*- coding: UTF-8 -*-

from apscheduler.schedulers.blocking import BlockingScheduler

def job():
    print('hello apscheduler')

scheduler = BlockingScheduler()

scheduler.add_job(job)
scheduler.add_job(job, 'cron', day_of_week='1-5', hour=6, minute=30)
scheduler.add_job(job, 'interval', seconds=2, id='test_job')

scheduler.start()