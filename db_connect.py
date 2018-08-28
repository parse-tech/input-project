import pymysql
import sql_login

def connect_to_db_cli():
    return pymysql.connect(db = "cli",
                           user = sql_login.user,
                           passwd = sql_login.password,
                           host = sql_login.host,
                           port = sql_login.port)

def connect_to_db_site_daily_log():
    return pymysql.connect(db = "website",
                           user = sql_login.user,
                           passwd = sql_login.password,
                           host = sql_login.host,
                           port = sql_login.port)