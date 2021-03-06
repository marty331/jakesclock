from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Required
from wtforms.widgets import HTMLString, html_params
#from flask.ext.wtf import fields, widgets, TextField
from datetime import datetime
from flask.ext.admin.form import widgets
from wtforms import fields, widgets, TextField, validators
from wtforms.fields.html5 import DateField, DateTimeField


class LoginForm(Form):
	remember_me = BooleanField('remember_me', default=False)

class EditForm(Form):
	nickname = StringField('nickname', validators=[DataRequired()])
	about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])

	def __init__(self, original_nickname, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.original_nickname = original_nickname

	def validate(self):
		if not Form.validate(self):
			return False 
		if self.nickname.data == self.original_nickname:
			return True

class PostForm(Form):
	post = StringField('post', validators=[DataRequired()])

class AlarmTime(Form):
    #dt = DateTimeField('TimePicker', format='%Y-%m-%d %H:%M')
    dt = StringField('alarmTime')
    days = StringField('days')
