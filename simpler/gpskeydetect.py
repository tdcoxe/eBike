
import os
from gps import *
from time import *
import time
import threading
import bluetooth
import time
import RPi.GPIO as GPIO
 
GPIO.setmode(GPIO.BOARD)
RELAY1 = 7
RELAY2 = 11
RELAY3 = 12
RELAY4 = 13
RELAY5 = 15
RELAY6 = 16
RELAY7 = 18
RELAY8 = 22
KEY = 38
GPIO.setup(RELAY1, GPIO.OUT)
GPIO.setup(RELAY2, GPIO.OUT)
GPIO.setup(RELAY3, GPIO.OUT)
GPIO.setup(RELAY4, GPIO.OUT)
GPIO.setup(RELAY5, GPIO.OUT)
GPIO.setup(RELAY6, GPIO.OUT)
GPIO.setup(RELAY7, GPIO.OUT)
GPIO.setup(RELAY8, GPIO.OUT)
GPIO.setup(KEY, GPIO.IN, GPIO.PUD_DOWN)
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    while True:
		tom =  bluetooth.lookup_name('94:65:2d:82:53:61', timeout=110)
		if ((tom != None) or (GPIO.input(38))):
			while (GPIO.input(38)):
				print "Key bypass engaged "  
				GPIO.output(RELAY1,0)
				GPIO.output(RELAY2,0)
				GPIO.output(RELAY3,0)
				GPIO.output(RELAY4,0)
				GPIO.output(RELAY5,0)
				GPIO.output(RELAY6,0)
				GPIO.output(RELAY7,0)
				GPIO.output(RELAY8,0)
				time.sleep(10)
				print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " + str(gpsd.fix.longitude)
			else:
				if (tom != None):
					print "Tom's here :)"
					GPIO.output(RELAY1,0)
					GPIO.output(RELAY2,0)
					GPIO.output(RELAY3,0)
					GPIO.output(RELAY4,0)
					GPIO.output(RELAY5,0)
					GPIO.output(RELAY6,0)
					GPIO.output(RELAY7,0)
					GPIO.output(RELAY8,0)
					time.sleep(10)
					print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " + str(gpsd.fix.longitude)
		else:
			print "Tom's gone :("
			GPIO.output(RELAY1,1)
			GPIO.output(RELAY2,1)
			GPIO.output(RELAY3,1)
			GPIO.output(RELAY4,1)
			GPIO.output(RELAY5,1)
			GPIO.output(RELAY6,1)
			GPIO.output(RELAY7,1)
			GPIO.output(RELAY8,1)
			time.sleep(10)
			print "Checking " + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()) + ",  " + str(gpsd.fix.latitude) + ",  " +  str(gpsd.fix.longitude)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
