#!/usr/bin/python
import os
import urllib
import sys
sys.path.insert(0, 'external')

sys.path.insert(0, 'libs')

import urllib2
import datetime
from time import gmtime
import re
import logging

#!/usr/bin/python

# Import modules for CGI handling 
import cgi, cgitb 
cgitb.enable()
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
#logging.info('form ='+form)
#print form
url = "http://10.0.0.5/"

def on_text(inp):
	s = open('/etc/motion/motion.conf').read()
	#print datetime.datetime.now()
	#print ('file contains:'+s)
	if (inp == 'living'):
		s = s.replace('; thread /etc/motion/thread1.conf', 'thread /etc/motion/thread1.conf')
	elif (inp == 'kitchen'):
		s = s.replace('; thread /etc/motion/thread2.conf', 'thread /etc/motion/thread2.conf')
	elif (inp == 'front'):
		s = s.replace('; thread /etc/motion/thread3.conf', 'thread /etc/motion/thread3.conf')
	elif (inp == 'back'):
		s = s.replace('; thread /etc/motion/thread4.conf', 'thread /etc/motion/thread4.conf')
	elif (inp == 'side'):
		s = s.replace('; thread /etc/motion/thread5.conf', 'thread /etc/motion/thread5.conf')
	else:
		print 'Error'
	f = open('/etc/motion/motion.conf', 'w')
	f.write(s)
	f.close()
	#print s

def off_text(inp):
	s = open('/etc/motion/motion.conf').read()
	#print datetime.datetime.now()
	#print ('file contains:'+s)
	re1='(;this is a test)'	# Any Single Character 1
	re2='(this is a test)'	# Word 1
	if (inp == 'living'):
		re1='(; thread /etc/motion/thread1.conf)'	# Any Single Character 1
		re2='(thread /etc/motion/thread1.conf)'	# Word 1
	elif (inp == 'kitchen'):
		re1='(; thread /etc/motion/thread2.conf)'	# Any Single Character 1
		re2='(thread /etc/motion/thread2.conf)'	# Word 1
	elif (inp == 'front'):
		re1='(; thread /etc/motion/thread3.conf)'	# Any Single Character 1
		re2='(thread /etc/motion/thread3.conf)'	# Word 1
	elif (inp == 'back'):
		re1='(; thread /etc/motion/thread4.conf)'	# Any Single Character 1
		re2='(thread /etc/motion/thread4.conf)'	# Word 1
	elif (inp == 'side'):
		re1='(; thread /etc/motion/thread5.conf)'	# Any Single Character 1
		re2='(thread /etc/motion/thread5.conf)'	# Word 1
	else:
		print 'Error'

	rg = re.compile(re1,re.IGNORECASE|re.DOTALL)
	m = rg.search(s)
	#print rg.search(s)
	if m:
		c1=m.group(1)
		logging.info(c1)
	else:
		if (inp == 'living'):
			s = s.replace('thread /etc/motion/thread1.conf', '; thread /etc/motion/thread1.conf')
		elif (inp == 'kitchen'):
			s = s.replace('thread /etc/motion/thread2.conf', '; thread /etc/motion/thread2.conf')
		elif (inp == 'front'):
			s = s.replace('thread /etc/motion/thread3.conf', '; thread /etc/motion/thread3.conf')
		elif (inp == 'back'):
			s = s.replace('thread /etc/motion/thread4.conf', '; thread /etc/motion/thread4.conf')
		elif (inp == 'side'):
			s = s.replace('thread /etc/motion/thread5.conf', '; thread /etc/motion/thread5.conf')
		else:
			loggin.info('error')
		f = open('/etc/motion/motion.conf', 'w')
		f.write(s)
		f.close()
		#print s

def redirect(url = None):
	host = os.environ.get('HTTP_HOST', '')
	if not host:
		host = os.environ.get('SERVER_NAME', 'localhost')
		port = os.environ.get('SERVER_PORT', '80')
	result = "%s://%s" %('http', host)
	result += url
	return result

# Get data from fields
if form.getvalue('livingcam'):
   living_flag = "ON"
   room = 'living'
   on_text(room)
else:
   living_flag = "OFF"
   room = 'living'
   off_text(room)
   # Get data from fields
if form.getvalue('kitchencam'):
   kitchen_flag = "ON"
   room = 'kitchen'
   on_text(room)
else:
   kitchen_flag = "OFF"
   room = 'kitchen'
   off_text(room)
   # Get data from fields
if form.getvalue('frontcam'):
   front_flag = "ON"
   room = 'front'
   on_text(room)
else:
   front_flag = "OFF"
   room = 'front'
   off_text(room)
   # Get data from fields
if form.getvalue('backcam'):
   back_flag = "ON"
   room = 'back'
   on_text(room)
else:
   back_flag = "OFF"
   room = 'back'
   off_text(room)
   # Get data from fields
if form.getvalue('sidecam'):
   side_flag = "ON"
   room = 'side'
   on_text(room)
else:
   side_flag = "OFF"
   room = 'side'
   off_text(room)

#print "Location: http://\n\n";
print "Status: 302 Moved"
print "Location: %s" % url
#print 'Location: http://localhost:8000/'
#print ("Location:http:localhost")
print # to end the CGI response headers.



