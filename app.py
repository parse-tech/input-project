from flask import Flask, render_template, redirect, url_for
import db_connect
import pymysql
import board_blog_forms
import db_actions
import back_end

app = Flask(__name__)
app.secret_key = 'nklfAEJiku0*()&ijlkdnlkmklLKHn..4lk4'

DEBUG = True
PORT = 8086
HOST = '0.0.0.0'

@app.route('/', methods=("GET", "POST"))
def display():
#    form = board_blog_forms.Test_Form()
#    if form.validate_on_submit():
#        db_actions.test_post(form.post)
    return render_template('base.html')

@app.route('/cli_information')
def cmd_list():
#    conn = db_connect.connect_to_db_cli()
#    cur = conn.cursor()
#    cur.execute('SELECT * FROM cmd')
#    results = cur.fetchone()
    form = board_blog_forms.New_CLI_Form()
    form.type.choices = [('', 'Select Type')] + list(db_actions.get_all_cli_types())
    form.category.choices = [('', 'Select Category')] + list(db_actions.get_all_cli_categories())
    if form.validate_on_submit():
        db_actions.create_new_cli_entry(form.command.data, form.action.data, form.type.data, form.category.data)
        return redirect(url_for('cli_information'))
    return render_template('cli_information.html', form=form, data=db_actions.get_all_cli_entries())

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = board_blog_forms.New_Blog_Post_Form()
    if form.validate_on_submit():
        # Adds Blog Post to DB
        db_actions.create_blog_post(form.title.data, form.post.data)
        # Gets a set of hashtags from back_end function and inserts them into the hashtag table
        db_actions.add_new_tag(back_end.get_hashtags(form.post.data))
    return render_template('blog.html', form=form, all_posts=db_actions.get_all_blog_posts())

@app.route('/daily_log', methods=['GET', 'POST'])
def daily_log():
    form = board_blog_forms.Daily_Log_Form()
    if form.validate_on_submit():
        db_actions.daily_post(form.post.data)
        return redirect(url_for('daily_log'))
    return render_template('daily_log.html', form=form, all_posts = db_actions.all_daily_posts())
'''
@app.rout('/message_board', methods=['GET', 'POST'])
def message_board():
    form = board_blog_forms.New_Message_Board_Post_Form()
    if form.validate_on_submit():
        db_actions.
'''
if __name__=='__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)
