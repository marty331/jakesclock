from flask import render_template, flash, redirect, session, url_for, request, g
from flask import render_template
from app import app, db
from flask import render_template, flash, redirect, request
from app import app
from .forms import AlarmTime
import logging
from logging.handlers import RotatingFileHandler
from .models import Alarms
from datetime import datetime
from crontab import CronTab

SECRET_KEY = "asdfhjgfdsyuhgfcxdsrethgf"
DEBUG = True

'''
@app.before_request
def before_request():

	alarms = Alarms.query.get(int(id))
	db.session.add(g.user)
	db.session.commit()
	'''

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
	logging.info("index")
	app.logger.info("index clicked")
	form = AlarmTime()
	alarmTime = 'Not set'
	
	if form.validate_on_submit():
		#alarmTime = form.dt.data.strftime('%H-%M'))
		now = datetime.now()
   		timeString = now.strftime("%H:%M")
   		#alarmTime = form.dt
   		alarmTime = request.form['my_list']
   		time_object = datetime.strptime(alarmTime, '%H:%M').time()
   		hourtime = int(time_object.hour)
   		mintime = int(time_object.minute)
   		#minTime = time_object.minute()
   		#app.logger.info('minute ='+str(time_object))
   		app.logger.info('time ='+str(time_object))
   		time_object = datetime.strptime(str(time_object), '%H:%M:%S').strftime('%I:%M %p').lower()
   		app.logger.info('time ='+str(time_object))
   		#monDay = str(request.form['cbMon'])
   		value = request.form.getlist('cbMon')
   		if alarmTime is None:
   			alarmTime = 'None'
   		app.logger.info('time ='+ alarmTime+ ' value ='+str(value))
   		app.logger.info(value)
		logging.info('time ='+ alarmTime+ ' timeString ='+timeString)
		#return form.dt.data.strftime('%Y-%m-%d')
		day = []
		for d in value:
			if d == 'Mon':
				day.append('MON')
			if d =='Tue':
				day.append('TUE')
			if d == 'Wed':
				day.append('WED')
			if d == 'Thu':
				day.append('THU')
			if d == 'Fri':
				day.append('FRI')
		days = ', '.join(value)
		#day = ['SUN', 'MON']
		app.logger.info('day ='+str(day))
		if days[:1] == ',':
			days = days.replace(days[:1], '')
		if days[-1:] == ',':
			days = days.replace(days[-1:], '')
		sound = request.form['soundList']
		sounds = ''
		if sound == 'good_morning.mp3':
			sounds = 'Good Morning'
		elif sound == 'frog.mp3':
			sounds = 'Frogs'
		elif sound =='soft_wake.mp3':
			sounds = 'Soft Wake'
		else:
			sounds = ''
		app.logger.info('soundlist ='+sound)
		if alarmTime is not None:
			#delete all existing alarm rows
			r = Alarms().query.all()
			for a in r:
				db.session.delete(a)
			db.session.commit()
			#add new alarm row
			post = Alarms(time=alarmTime, days=days, sounds=sounds)
			db.session.add(post)
			db.session.commit()
			flash('Your alarm is now set!')
			
			cron    = CronTab()
			#croncommand = '/usr/bin/python /home/marty331/Python/jake/app/'+sound
			croncommand = '/usr/bin/mpg123 /home/marty331/Python/jake/sounds/'+sound
			x = 0
			job= []
			for n in range(len(day)):
				j = 'job'+chr(ord('A')+n)
				d = day[n]
				j = cron.new(command=croncommand)
				j.minute.on(mintime)
				j.hour.on(hourtime)
				j.dow.on(d)
			'''
			for d in day:
				job+x = cron.new(command=croncommand)
				job+x.minute.on(mintime)
				job[x].hour.on(hourtime)
				job[x].dow.on(d)
				x +=1
			'''
			cron.write()
			
			return redirect(url_for('index'))
	alarms = Alarms().query.all()
	if len(alarms)==0:
		mins = 0
		hours = 0
	for a in alarms:
		mins = datetime.strptime(a.time, '%H:%M').time()
		hours = datetime.strptime(str(mins), '%H:%M:%S').strftime('%I:%M %p').lower()
	return render_template('index.html', timeset=alarmTime, title='Jake\'s Clock page', form=form, times=hours, alarms=alarms)
