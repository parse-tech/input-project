from flask_wtf import Form
from wtforms import StringField, PasswordField, TextAreaField, SelectField, BooleanField, IntegerField
from wtforms.validators import (DataRequired, Regexp, ValidationError, Email,
                                Length, EqualTo, InputRequired)
from wtforms.fields.html5 import DateField

class Daily_Log_Form(Form):
    post = TextAreaField("Post", validators=[DataRequired()])
    
class New_CLI_Form(Form):
    command = StringField("Command", validators=[DataRequired()])
    action = StringField("Action", validators=[DataRequired()])
    type = SelectField("Type", coerce=int)
    category = SelectField("Category", coerce=int)

class New_Blog_Post_Form(Form):
    title = StringField("TITLE", validators=[DataRequired()])
    post = TextAreaField("POST", validators=[DataRequired()])

class New_Message_Board_Post_Form(Form):
    post = TextAreaField("Message", validators=[DataRequired()])

class Search_Log_Form(Form):
    word = StringField("Search word/phrase", validators=[DataRequired()])


class Part_Order_Form(Form):
    employee = SelectField("Employee", coerce=int)
    p_client = SelectField("Client", coerce=int)
    part_id = SelectField("Part", coerce=int)
    p_retailer = SelectField("Retailer", coerce=int)
    p_store = SelectField("Store", coerce=int)
    order_date = DateField("Order Date", validators=[InputRequired()], format="%m/%d/%Y")