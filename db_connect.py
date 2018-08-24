import pymysql

def connect_to_db_cli():
    return pymysql.connect(db = "cli",
                                 user = "moking",
                                 passwd = "P1Xac4u",
                                 host = "0.0.0.0",
                                 port = 3306)

def connect_to_db_site_dailiy_log():
    return pymysql.connect(db = "website",
                           user = "moking",
                           passwd = "P1Xac4u",
                           host = "0.0.0.0",
                           port = 3306)