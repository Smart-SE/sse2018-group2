# -*- coding: utf-8 -*-
import sqlite3


def read_table(dbname,dbtable):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()

    select_sql = 'select * from t_temp'
    for row in c.execute(select_sql):
        print(row)

    conn.close()


if __name__ =='__main__':

    dbname = '/home/pi/temp.db'

    dbtable = 't_temp'

    read_table(dbname,dbtable)
