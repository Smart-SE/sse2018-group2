import requests
from datetime import datetime

#ここへEvent名を入れる
EVENT_NAME = 'XXXXXX'
#ここへ、Webhookのキーを入れる。
IFTTT_KEY = 'XXXXXXXXXXXXXXXXXXXXX-XXXXXX'
IFTTT_FROM_WEBHOOK_TO_LINE = 'https://maker.ifttt.com/trigger/'+EVENT_NAME+'/with/key/'

#Line側の設定をデフォルトのまま使えば下記関数でそのまま利用可能
def LineNotify(time, valueA, valueB):
	requests.post(IFTTT_FROM_WEBHOOK_TO_LINE + IFTTT_KEY, json = {"value1":time, "value2":valueA, "value3":valueB})

while 1:
	LineNotify(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'testA','testB')
