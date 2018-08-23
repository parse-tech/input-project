from __future__ import print_function

import calculate_distance
import db_connect
import json
import pymysql
import re
from datetime import *
from dateutil.parser import parse
import os

conn = db_connect.connect_to_db()
cur = conn.cursor()

def daily_post(content):
    if verify_new_part_order(part_id, store_id):
        sql = "INSERT INTO  daily_log (content, submit_time)" \
              " VALUES (" + str(content) + ", NOW())"
        cur.execute(sql)
        conn.commit()
        return True
    else:
        return False