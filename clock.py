import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
import urllib.request
sched = BlockingScheduler()




@sched.scheduled_job('cron', minute='*/2')
def scheduled_job():
    print('========== APScheduler CRON =========')
    # 馬上讓我們瞧瞧
    print('This job runs every day */2 min.')
    # 利用datetime查詢時間
    print(f'{datetime.datetime.now().ctime()}')
    print('========== APScheduler CRON =========')
    
sched.start()
