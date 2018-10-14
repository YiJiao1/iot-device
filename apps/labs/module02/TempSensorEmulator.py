'''
Created on 2018年9月15日
 
@author: heychris
'''

from random import uniform
from time import sleep
from threading import Thread
from labs.common.SensorData import SensorData
from labs.module02 import SmtpClientConnector


class TempSensorEmulator(Thread): 
    alertDiff = 5 
    curTemp = \
    max_value = 0
    min_value = 0
    enableTempEmulator = False
    maxUpdateTime = 0
    minUpdatetime = 0
    tempSensorData = SensorData("Temperature")
    emailSender = None
    isPrevTempSet = False
    rateInSec      = 5

# constructor which get 4 reference
    def __init__(self, max_temp, min_temp, max_updateTime, min_updateTime):
        Thread.__init__(self)
        self.max_value = max_temp
        self.min_value = min_temp
        self.maxUpdateTime = max_updateTime
        self.minUpdatetime = min_updateTime
         
    def getCurrValue(self):
        return self.curTemp
    
#     TempSensorEmulator thread which  gets newTemp around min / max updatetime(In this part we set the time is 5 sec)
#      thread to calculate the curVal exceeds average than 5.

    def run(self):
        while True:
            if self.enableTempEmulator:
                if self.isPrevTempSet == False:
                    # corner code
                    self.prevTemp = self.curTemp
                    self.isPrevTempSet = True
                else:
                    self.curTemp = uniform(float(self.min_value), float(self.max_value))
                    self.tempSensorData.addNewValue(self.curTemp)
                    print('----------------------------')
                    print('New sensor readings:')
                    print(str(self.tempSensorData))
                    if abs(self.tempSensorData.avgTemp - self.tempSensorData.curTemp) > 5:
                        print("Current temp exceeds average by >" + str(abs(self.tempSensorData.avgTemp - self.curTemp)))
                        # config data path
                        path = "../../../data/ConnectedDevicesConfig.props"
                        # new SmtpClientConnector instance add path
                        emailSender = SmtpClientConnector.SmtpClientConnector(path)
                        emailSender.sendEmailMessage("TemperatureEmulator(Exceptional)", self.tempSensorData)
                        print("")
                sleep(self.rateInSec)

# unit test part
# emulator=TempSensorEmulator(36,-10, 5, 4)
# emulator.enableTempEmulator=True
# while True:
#     print("CurrentTemperature:"+str(emulator.getCurrValue()))
#     emulator.run();
#     sleep(3)
