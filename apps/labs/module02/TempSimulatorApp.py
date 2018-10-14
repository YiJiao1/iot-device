'''
Created on 2018年9月15日
cswfwfw
@author: heychris
'''
from time import sleep
from labs.module02.TempSensorEmulator import TempSensorEmulator

# new TempSensorEmulator instance 
tempSensor = TempSensorEmulator(30, 0, 4, 1)

# open the enableTempEmulator
tempSensor.enableTempEmulator = True
tempSensor.daemon=True
# start enableTempEmulator thread
tempSensor.start()



# main thread run
while True:
    sleep(10)
    pass