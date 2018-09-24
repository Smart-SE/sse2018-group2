import requests
from datetime import datetime

#������Event��������
EVENT_NAME = 'XXXXXX'
#�����ցAWebhook�̃L�[������B
IFTTT_KEY = 'XXXXXXXXXXXXXXXXXXXXX-XXXXXX'
IFTTT_FROM_WEBHOOK_TO_LINE = 'https://maker.ifttt.com/trigger/'+EVENT_NAME+'/with/key/'

#Line���̐ݒ���f�t�H���g�̂܂܎g���Ή��L�֐��ł��̂܂ܗ��p�\
def LineNotify(time, valueA, valueB):
	requests.post(IFTTT_FROM_WEBHOOK_TO_LINE + IFTTT_KEY, json = {"value1":time, "value2":valueA, "value3":valueB})

while 1:
	LineNotify(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'testA','testB')
