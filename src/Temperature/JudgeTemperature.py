#-*- coding: utf-8 -*-
import sys
import os
import pandas as pd
from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../util')
import FromWebhookToLine

dateparse = lambda x: pd.datetime.strptime(x, '%Y/%m/%d %H:%M:%S')
df = pd.read_csv('test.csv', header=None, names=['datetime', 'deviceID', 'temperature'], parse_dates=['datetime'], date_parser=dateparse)

#for i, r in df.iterrows():
#    print type(r['datetime']), type(r['deviceID']), type(r['temperature'])

df_s = df.sort_index(axis=0, ascending=False)

#print(df_s)
#print(df_s.head(1))
#print(df_s.iloc[0])
print("Temperature:%6.2f" % df_s['temperature'].values[0])

if (df_s['temperature'].values[0] >= 20):
#  print("over limit")
   LineNotify(datetime.now().strftime("%Y/%m/%d %H:%M:%S"),'SensorID','温かくなっています')
