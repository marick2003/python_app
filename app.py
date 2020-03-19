import datetime
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import os, sys
from flask import Flask, request, abort, jsonify

import requests

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
# Channel Access Token
line_bot_api = LineBotApi(channel_access_token)
# Channel Secret
handler = WebhookHandler(channel_secret)

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text

    message = ImagemapSendMessage(
    base_url='https://example.com/base',
    alt_text='this is an imagemap',
    base_size=BaseSize(height=1040, width=1040),
    actions=[
            URIImagemapAction(
                link_uri='https://example.com/',
                area=ImagemapArea(
                    x=0, y=0, width=520, height=1040
                )
            ),
            MessageImagemapAction(
                text='hello',
                area=ImagemapArea(
                    x=520, y=0, width=520, height=1040
                )
            )
        ]
    )


    if input_text == '@查詢匯率':
        resp = requests.get('https://tw.rter.info/capi.php')
        currency_data = resp.json()
        usd_to_twd = currency_data['USDTWD']['Exrate']
        print(event.reply_token)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}'))
    if input_text == '@UID':
        obj=event
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'LINE Detail:{obj}'))
    if input_text == '@TEST':
         line_bot_api.reply_message(
            event.reply_token,
            message)
        

# scheduler = BlockingScheduler() 
# def job_task(): 
#     print "%s: 執行任務" % time.asctime() 
#     # 添加任務並設置觸發方式為3s一次 
#     scheduler.add_job(job_task, 'interval', seconds=3) 
#     # 開始運行調度器
# scheduler.start()
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True, host='0.0.0.0', port=port)