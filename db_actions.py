from __future__ import print_function

#import calculate_distance
import db_connect
#import json
import pymysql
#import re
from datetime import *
#from dateutil.parser import parse
import os

#conn = db_connect.connect_to_db()
#cur = conn.cursor()

def daily_post(content):
    conn = db_connect.connect_to_db_site_dailiy_log()
    cur = conn.cursor()
    sql = "INSERT INTO  daily_log (content, submit_time)" \
          " VALUES (" + str(content) + ", NOW())"
    cur.execute(sql)
    conn.commit()
    return True
