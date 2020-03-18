# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )

# app = Flask(__name__)

# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('9f737ae6235a4b78d2db6ca9f097b5e7', None)
# channel_access_token = os.getenv('UJFzuSiw3bjf+ODolRmWgzBm9iAEVnQpWeoCMpWgB9ybewND1qzq3mEI5iYZ/08Sv0oGw0xMiem4r3PS7lSIbyMFeoAD9BB1NC2u/UYb7ed/s6aBdS7xVSFn6OkV5xnYO+RW0pUu74YFkNJaUfYtTgdB04t89/1O/w1cDnyilFU=', None)
# if channel_secret is None or channel_access_token is None:
#     print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
#     sys.exit(1)

# line_bot_api = LineBotApi(channel_access_token)
# handler = WebhookHandler(channel_secret)

# # 此為 Webhook callback endpoint
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body（負責）
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)

#     return 'OK'

# # decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # 決定要回傳什麼 Component 到 Channel
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


# if __name__ == '__main__':
#     app.run()
# import os
# import sys

# from flask import Flask, request, abort

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )
# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )

# app = Flask(__name__)

# # get channel_secret and channel_access_token from your environment variable
# channel_secret = os.getenv('9f737ae6235a4b78d2db6ca9f097b5e7', None)
# channel_access_token = os.getenv('UJFzuSiw3bjf+ODolRmWgzBm9iAEVnQpWeoCMpWgB9ybewND1qzq3mEI5iYZ/08Sv0oGw0xMiem4r3PS7lSIbyMFeoAD9BB1NC2u/UYb7ed/s6aBdS7xVSFn6OkV5xnYO+RW0pUu74YFkNJaUfYtTgdB04t89/1O/w1cDnyilFU=', None)
# if channel_secret is None or channel_access_token is None:
#     print('Specify LINE_CHANNEL_SECRET and LINE_CHANNEL_ACCESS_TOKEN as environment variables.')
#     sys.exit(1)

# line_bot_api = LineBotApi(channel_access_token)
# handler = WebhookHandler(channel_secret)

# # 此為 Webhook callback endpoint
# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body（負責）
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         print("Invalid signature. Please check your channel access token/channel secret.")
#         abort(400)

#     return 'OK'

# # decorator 負責判斷 event 為 MessageEvent 實例，event.message 為 TextMessage 實例。所以此為處理 TextMessage 的 handler
# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     # 決定要回傳什麼 Component 到 Channel
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


# if __name__ == '__main__':
#     app.run()

import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




