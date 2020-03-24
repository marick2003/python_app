# from apscheduler.schedulers.blocking import BlockingScheduler 
# # 實例化一個調度器
# scheduler = BlockingScheduler() 
# def job_task(): 
#     print("123")
#    # 添加任務並設置觸發方式為3s一次 
#     scheduler.add_job(job_task, 'interval', seconds=3) 
#    # 開始運行調度器
# scheduler.start()

from fuzzywuzzy import fuzz
Str1 = "Apple Inc."
Str2 = "apple Inc"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
print(Ratio)

import os, sys
from flask import Flask, request, abort, jsonify
import requests
from bs4 import BeautifulSoup

# resp = urllib2.urlopen('https://forex.cnyes.com/currency/JPY/TWD')
# soup = BeautifulSoup(resp, 'html.parser')
# print(soup.find('input')['name'], ':', soup.find('input')['value'])


import requests
from bs4 import BeautifulSoup
import math
#currency-number currency-now
resp = requests.get('https://forex.cnyes.com/currency/JPY/TWD')
soup = BeautifulSoup(resp.text, 'html5lib')
_ans=soup.find('div',class_="currency-now")
_num=_ans.text
print(int(_num*100))