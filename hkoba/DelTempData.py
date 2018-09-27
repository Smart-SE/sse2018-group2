# -*- coding: utf-8 -*-
import sqlite3


def del_table(dbname,dbtable):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    sql = "drop table "+dbtable
    c.execute(sql,)
    conn.commit()


if __name__ =='__main__':

    dbname = '/home/pi/temp.db'

    dbtable = 't_temp'

    del_table(dbname,dbtable)
