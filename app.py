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
#模糊比對
from fuzzywuzzy import fuzz
#
from bs4 import BeautifulSoup

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
        #stock button
        # message = TemplateSendMessage(
        #     alt_text='Buttons template',
        #     template=ButtonsTemplate(
        #         thumbnail_image_url='https://example.com/image.jpg',
        #         title='Menu',
        #         text='Please select',
        #         actions=[
        #             PostbackTemplateAction(
        #                 label='postback',
        #                 text='postback text',
        #                 data='action=buy&itemid=1'
        #             ),
        #             MessageTemplateAction(
        #                 label='message',
        #                 text='message text'
        #             ),
        #             URITemplateAction(
        #                 label='uri',
        #                 uri='http://example.com/'
        #             )
        #             ]
        #         )
        # )
        #check button
    message=TemplateSendMessage(
             alt_text='查詢匯率',
             template=ButtonsTemplate(
                 thumbnail_image_url='https://example.com/image.jpg',
                 title='Menu',
                 text='Please select',
                  actions=[
                    MessageTemplateAction(
                        label='美金匯率',
                        text='美金匯率'
                    ),
                    MessageTemplateAction(
                        label='澳幣匯率',
                        text='澳幣匯率'
                    ),
                    MessageTemplateAction(
                        label='日幣匯率',
                        text='日幣匯率'
                    ),
                  ]
             )
        )     
    if fuzz.ratio(input_text,"查詢匯率")>=80:
        # resp = requests.get('https://tw.rter.info/capi.php')
        # currency_data = resp.json()
        # usd_to_twd = currency_data['USDTWD']['Exrate']
        # print(event.reply_token)
        # line_bot_api.reply_message(
        #     event.reply_token,
        #     TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}'))
        line_bot_api.reply_message(
              event.reply_token,message
         )

    if fuzz.ratio(input_text,"美金匯率")>=80:
        resp = requests.get('https://tw.rter.info/capi.php')
        currency_data = resp.json()
        usd_to_twd = currency_data['USDTWD']['Exrate']
        print(event.reply_token)
        line_bot_api.reply_message(
             event.reply_token,
             TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}'))
    
    if fuzz.ratio(input_text,"日幣匯率")>=80:
        resp = requests.get('https://forex.cnyes.com/currency/JPY/TWD')
        soup = BeautifulSoup(resp.text, 'html5lib')
        _ans=soup.find('div',class_="currency-now")
       
        print(_ans)
        line_bot_api.reply_message(
             event.reply_token,
             TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{ _ans.text*100}'))

    if fuzz.ratio(input_text,"澳幣匯率")>=80:
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
    if input_text == '@周子揚':
         line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='小GG'))
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    # app.run(host='0.0.0.0', port=port)
    app.run(debug=True, host='0.0.0.0', port=port)