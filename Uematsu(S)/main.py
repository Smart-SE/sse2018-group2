import TemperatureModule
import FileModule
from datetime import datetime
import time

sensorID = '28-000f98432706'
fileName = 'test.csv'

FileModule.Clear(fileName)

while 1:
	temperature = TemperatureModule.Get(sensorID)
	timeStump = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	output = timeStump + ',' + sensorID + ',' + str(temperature)
	FileModule.AddRow(fileName, output.split(','))
	print output.split(',')

	#time.sleep(4)

