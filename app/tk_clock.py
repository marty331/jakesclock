#!flask/bin/python

import time
from Tkinter import *
import logging
#from flask import Flask


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

#root=tk.Tk()
#app=FullScreenApp(root)
#root.mainloop()



root = Tk()
app=FullScreenApp(root)
#root.resizable(width=FALSE, height=FALSE)
#root.geometry(("%dx%d")%(800, 480))
root.wm_title('Jake\'s Clock')
#root.overrideredirect(1)

time1 = ''
clock = Label(root, font=('times', 60, 'bold'), bg='green', fg='white')
alarm = Label(root, font=('times', 20, 'bold'), bg='green')
#name = Label(root, font=('times', 20, 'bold'), bg='green')
#name.pack(fill=BOTH, expand=1)
clock.pack(fill=BOTH, expand=1)
alarm.pack(fill=BOTH, expand=1)
al = 'Alarm: '
at = 'No Alarm'

def tick():
    global time1
    time2 = time.strftime('%I'+":"+'%M'+':'+'%S'+' '+'%p')
    if time2 != time1:
        time1 = time2
        #name.config(text='Jake\'s Clock')
        clock.config(text=time2)
        alarm.config(text=al+at)
    clock.after(200,tick)
tick()
root.mainloop()

