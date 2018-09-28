#import time

def Get(sensorID):
	tempfile = open ("/sys/bus/w1/devices/" + sensorID + "/w1_slave") 
	#please replace  28-000f98432706 with your sensor address from tutorial step 5
	
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature /1000
	return temperature
