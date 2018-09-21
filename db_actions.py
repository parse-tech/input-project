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
    conn_site.commit()
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

def get_all_blog_posts():
    cur_site.execute("SELECT * FROM blog")
    return cur_site.fetchall()

def get_specific_blog_post(post):
    cur_site.execute("SELECT * FROM blog WHERE post_id=" + str(post))
    return cur_site.fetchall()

# When create message board site
#def get_message_board_posts():
#    cur_site.execute("SELECT * FROM ")

def create_blog_post(title, content):
    cur_site.execute("INSERT INTO blog (title, content, submit_time) VALUES ('" + title + "', '" + content + "', NOW())")
    conn_site.commit()
    return True

def increment_tag_count(hashtag):
    cur_site.execute("SELECT count FROM hashtags WHERE tag LIKE '" + hashtag + "'")
    tag_count = cur_site.fetchone()
    #tag_count[0]+=1
    count = int(tag_count[0])
    count+=1
    cur_site.execute("UPDATE hashtags SET count = " + str(count) + " WHERE tag LIKE '" + hashtag + "'")
    conn_site.commit()
    return True

# Returns True there are any new hashtags and False if there are no new hashtags
def add_new_tag(hashtags):
    new_tag=False
    for tag in hashtags:
        cur_site.execute("SELECT * FROM hashtags WHERE tag='" + tag + "'")
        if cur_site.fetchone():
            increment_tag_count(tag)
            new_tag=True
        else:
            cur_site.execute("INSERT INTO hashtags (tag, count) VALUES ('" + str(tag) + "', 1)")
            conn_site.commit()
    return new_tag

def get_daily_log_by_word(word):
    cur_site.execute("SELECT * FROM daily_log WHERE MATCH (content) AGAINST ('" + str(word) + "')")
    return cur_site.fetchall()