from __future__ import print_function

#import calculate_distance
import db_connect
#import json
import pymysql
#import re
from datetime import *
#from dateutil.parser import parse
import os
import re

#conn = db_connect.connect_to_db()
#cur = conn.cursor()

conn_cli = db_connect.connect_to_db_cli()
cur_cli = conn_cli.cursor()

conn_site = db_connect.connect_to_db_site_daily_log()
cur_site = conn_site.cursor()

def daily_post(content):
#    conn = db_connect.connect_to_db_site_daily_log()
#    cur = conn.cursor()
    sql = "INSERT INTO  daily_log (content, post_date)" \
          " VALUES ('" + re.escape(content) + "', NOW())"
    cur_site.execute(sql)
    cur_site.commit()
    return True

def all_daily_posts():
#    conn = db_connect.connect_to_db_site_daily_log()
#    cur = conn.cursor()
    sql = "SELECT * FROM daily_log"
    cur_site.execute(sql)
    return cur_site.fetchall()

def get_all_cli_types():
    cur_cli.execute("SELECT id, type FROM types")
    return cur_cli.fetchall()

def get_cli_type(id):
    cur_cli.execute("SELECT type FROM types WHERE id=" + str(id))
    return cur_cli.fetchone()

def get_cli_category(id):
    cur_cli.execute("SELECT category FROM categories WHERE id=" + str(id))

def get_all_cli_categories():
    cur_cli.execute("SELECT id, category FROM categories")
    return cur_cli.fetchall()

def get_all_cli_entries():
    cur_cli.execute("SELECT * FROM all_commands")
    return cur_site.fetchall()

def create_new_cli_entry(command, action, type, category):
    sql = "INSERT INTO all_commands (command, action, type, category) VALUES ('" + re.escape(command) + \
          "', '" + re.escape(action) + "', " + type + ", " + category + ")"
    cur_cli.execute(sql)
    conn_cli.commit()
    return True
