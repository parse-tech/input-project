from flask import Flask, render_template, redirect, url_for
import db_connect
import pymysql
import board_blog_forms
import db_actions

app = Flask(__name__)
app.secret_key = 'nklfAEJiku0*()&ijlkdnlkmklLKHn..4lk4'

DEBUG = True
PORT = 8086
HOST = '0.0.0.0'

@app.route('/', methods=("GET", "POST"))
def display():
    form = board_blog_forms.Test_Form()
    if form.validate_on_submit():
        db_actions.test_post(form.post)
    return render_template('base.html', form=form)

@app.route('/cmd_list')
def cmd_list():
    conn = db_connect.connect_to_db_cli()
    cur = conn.cursor()
    cur.execute('SELECT * FROM cmd')
    results = cur.fetchone()
    return render_template('cmd_list.html', words=results)

@app.route('/message_board')
def message_board():
    return render_template('message_board.html')

@app.route('/daily_log', methods=['GET', 'POST'])
def daily_log():
    form = board_blog_forms.Daily_Log_Form()
    if form.validate_on_submit():
        db_actions.daily_post(form.post.data)
        return redirect(url_for('daily_log'))
    return render_template('daily_log.html', form=form)

'''
@web_app.route('/parts/new_order', methods=['GET', 'POST'])
def new_part_order():
    form = part_forms.Part_Order_Form()
    form.employee.choices = [('0', 'Employee')] + list(app.get_all_employee_names())
    form.p_client.choices = [('0', 'Select Client')] + list(app.get_all_clients())
    form.part_id.choices = [('0', 'Select Part')] + list(part_order_app.get_all_parts_simple())
    form.p_retailer.choices = [('0', 'Select Retailer')] + list(app.get_all_retailers())
    form.p_store.choices = [('0', 'Select Store')] + list(app.get_all_stores())
    if form.validate_on_submit():
        if part_order_app.new_part_order(form.employee.data,
                                         form.p_client.data,
                                         form.part_id.data,
                                         form.p_store.data,
                                         form.order_date.data):
            return redirect(url_for('new_part_order'))
    return render_template('parts/new_part_order.html', time=datetime.datetime.now(), form=form)
    
    
    def new_part_order(ordered_by, client, part_id, store_id, order_date):
    if verify_new_part_order(part_id, store_id):
        sql = "INSERT INTO parts_orders (ordered_by, client, part_id, store_id, order_date)" \
            " VALUES (" + str(ordered_by) + ", " + str(client) + ", " + "'" + str(part_id) + "'," \
            " '" + str(store_id) + "', '" + date.strftime(order_date, '%Y-%m-%d') + "')"
        cur.execute(sql)
        conn.commit()
        write_to_json('order')
        return True
    else:
        return False
'''

if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
