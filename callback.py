#coding: utf-8

import requests
import json

REPLY_ENDPOINT = u"https://api.line.me/v2/bot/message/reply"

def post_text(reply_token, text):
    header = {
        "Content-Type": u"application/json",
        "Authorization": u"Bearer {ENTER_ACCESS_TOKEN}"
        }
    payload = {
        "replyToken":reply_token,
        "messages":[{"type":"text", "text":text}]
    }
    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))