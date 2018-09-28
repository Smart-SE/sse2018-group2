import requests
#from datetime import datetime

#¿¿¿Event¿¿¿¿¿
EVENT_NAME = 'XXXXXX'
#¿¿¿¿Webhook¿¿¿¿¿¿¿¿
IFTTT_KEY = 'XXXXXXXXXXXXXXXXXXXXX-XXXXXX'
IFTTT_FROM_WEBHOOK_TO_LINE = 'https://maker.ifttt.com/trigger/'+EVENT_NAME+'/with/key/'

#Line¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿
def LineNotify(time, valueA, valueB):
	requests.post(IFTTT_FROM_WEBHOOK_TO_LINE + IFTTT_KEY, json = {"value1":time, "value2":valueA, "value3":valueB})

#while 1:
#    LineNotify(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'SensorID','¿¿¿¿¿¿¿¿')
