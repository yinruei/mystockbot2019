#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('WP2GCZ7d787khmmhAc8+XL/uOOnxw6R77remJw70oVXW/OseZ50h+mxVJ+uxz4+GR0QBDdzYTVEY5FDErDgtCbzhQESWJPrOwjn0VDn9gFqxWnN25quJlRYL4FctUnH/5v2jdst85TphX1kpwzSJpwdB04t89/1O/w1cDnyilFU=
')
# 必須放上自己的Channel Secret
handler = WebhookHandler('6d6c01095d4740a7cff0ac88e3c77802')

line_bot_api.push_message('Ua91a8e4950a3b047f66ad093c81bdd70', TextSendMessage(text='你可以開始了'))

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

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
