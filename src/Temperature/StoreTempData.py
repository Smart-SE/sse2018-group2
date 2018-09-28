# -*- coding: utf-8 -*-
import sqlite3
import datetime

def Insert(TIME, DEVICE, TEMP, STATUS):

    #print("Last valid input: " + TIME)
    #print("Temperature: %f C" % TEMP)
    #print("DeviceID: " + DEVICE)
    #print("Status: %d" % STATUS)

    dbname = '/home/pi/temp.db'

    dbtable = 't_temp'

    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    checkdb = conn.execute("SELECT * FROM sqlite_master WHERE type='table' and name='%s'" % dbtable)

    if checkdb.fetchone() == None:
        create_table = '''create table ''' + dbtable + '''(id integer primary key autoincrement, timestamp varchar(20) not null, device text not null, temp real not null, status integer not null)'''
        c.execute(create_table)
        conn.commit()

    sql = 'insert into t_temp (timestamp, device, temp, status) values (?,?,?,?)'
    data = (TIME, DEVICE, TEMP, STATUS)
    c.execute(sql, data)
    conn.commit()

    conn.close()
