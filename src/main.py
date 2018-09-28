import Temperature.TemperatureModule as TM
import util.FileModule as FM
from datetime import datetime
import time

sensorID = '28-000f98432706'
fileName = 'test.csv'

FM.Clear(fileName)

while 1:
	temperature = TM.Get(sensorID)
	timeStump = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
	output = timeStump + ',' + sensorID + ',' + str(temperature)
	FM.AddRow(fileName, output.split(','))
	print output.split(',')

	time.sleep(4)

