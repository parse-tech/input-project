from flask import Flask, render_template
import db_connect
import pymysql

app = Flask(__name__)

DEBUG = True
PORT = 8086
HOST = '0.0.0.0'

conn = db_connect.connect_to_db_cli()
cur = conn.cursor()

@app.route('/')
def display():

    return render_template('base.html')

@app.route('/cmd_list')
def cmd_list():
    cur.execute('SELECT * FROM cmd')
    results = cur.fetchone()
    return render_template('cmd_list.html', words=results)

@app.rout('/message_board')
def message_board():
    return render_template('message_board.html')

if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
