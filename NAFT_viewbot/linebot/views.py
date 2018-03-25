from django.shortcuts import render
from django.http import HttpResponse
import json
import sys
import requests
import doco.client
import pandas
import codecs
import csv

# Create your views here.
REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
ACCESS_TOKEN = 'Enter your LINE ACCESS TOKEN'
FILE_ID = "Enter the Google Drive ID of the photo"

#test
def index(request):
    return HttpResponse("This is bot api.")

#request受信
def callback(request):
    reply = ""
    request_json = json.loads(request.body.decode('utf-8')) # requestの情報をdict形式で取得
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']   # typeの取得

        if message_type == 'text' or message_type == 'image' or message_type == 'sticker':
            reply += reply_img(reply_token)   # LINEにセリフを送信する関数
    return HttpResponse(reply) #views.pyはこれをreturnしないといけないらしい

def reply_img(reply_token):
    image_url = "https://drive.google.com/uc?export=view&id=" + FILE_ID
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + ACCESS_TOKEN
    }
    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"image",
                    "originalContentUrl":image_url,
                    "previewImageUrl":image_url
                }
            ]
    }
    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))
    return "ok"
