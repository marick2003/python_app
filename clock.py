import datetime
import urllib.request

from urllib import request, parse


import twstock
import requests

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler() 

stock_list = [
    '2330',  # 台積電
    '2317',  # 鴻海
    '1301',  # 台塑
    '1326',  # 台化
    '2412',  # 中華電
    '3008',  # 大立光
    '1303',  # 南亞
    '2308',  # 台達電
    '2454',  # 聯發科
    '2881',  # 富邦金
    '8299',  # 群聯
    '6223',
]
stock_name = {
    '2330': u'台積電',
    '2317': u'鴻海',
    '1301': u'台塑',
    '1326': u'台化',
    '2412': u'中華電',
    '3008': u'大立光',
    '1303': u'南亞',
    '2308': u'台達電',
    '2454': u'聯發科',
    '2881': u'富邦金',
    '8299': u'群聯',
    '6223': '旺矽'
}



@sched.scheduled_job('cron', minute='*/2')
def scheduled_job():
    print('========== APScheduler CRON =========')
    # 馬上讓我們瞧瞧
    print('This job runs every day */2 min.')
    # 利用datetime查詢時間
    print(f'{datetime.datetime.now().ctime()}')
    print('========== Sreach Stock =========')
    stock = twstock.Stock('2317')  
    print(stock)
    print('========== APScheduler CRON =========')
    
    #由於 Heroku 的免費方案會讓 dyno 在 30 分鐘無人打擾之後陷入沉睡狀態，
    #造成下次呼叫時需要較長的喚醒時間，而導致較差的使用者體驗➀。
    #為了能夠讓 Heroku 保持清醒狀態，我們用 APScheduler 讓我們的免費 dyno 在快要睡著的時候，呼叫 "https://你-APP-的名字.herokuapp.com/" ，自己喚醒自己。
    #不僅不發薪水，還要 Heroku 全天候工作，我們還真是個慣老闆啊。
    url = "https://pythonline2020.herokuapp.com/"
    conn = urllib.request.urlopen(url)
       
    for key, value in conn.getheaders():
        print(key, value)

sched.start()
