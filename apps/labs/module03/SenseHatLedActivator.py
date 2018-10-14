'''
Created on 2018年10月8日
 
@author: heychris
'''
from time import sleep
from sense_hat import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    enableLed = False
    rateInSec = 1
    rotateDeg = 270
    sh = None
    displayMsg = None
    
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
        
    def showLEDMessage(self,message,showingTime):
        self.displayMsg=message
        self.showingTime=showingTime
        self.enableLED=True #Start the thread
    
#     When temperature lower open led display
    def run(self):
        while True:
            count = 0
            if self.enableLed:
                print("Sensehat Led open!")
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                    count = count + 1
                if count > 3:
                    self.enableLed =False
            sleep(5)
 
 
    def getRateInSeconds(self):
        return self.rateInSec
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
        
    def setDisplayMessage(self, msg):
        self.displayMsg = msg