import os, sys
from flask import Flask, request, abort, jsonify

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('UJFzuSiw3bjf+ODolRmWgzBm9iAEVnQpWeoCMpWgB9ybewND1qzq3mEI5iYZ/08Sv0oGw0xMiem4r3PS7lSIbyMFeoAD9BB1NC2u/UYb7ed/s6aBdS7xVSFn6OkV5xnYO+RW0pUu74YFkNJaUfYtTgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9f737ae6235a4b78d2db6ca9f097b5e7')

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
    if input_text == '@查詢匯率':
        message = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token, message)
    
    


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
