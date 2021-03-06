'''
Created on 2018年10月8日

@author: heychris
'''

from labs.module03 import SimpleLedActivator
from labs.module03 import SenseHatLedActivator
from labs.common import ActuatorData


class TempActuatorEmulator:
     
    tempActuatorData = None    
    ledActivator = None
    LedActivator = None

#     open 2 threads (simple LED and senseHat LED)
    def __init__(self, blinkingTime):
        self.tempActuatorData = ActuatorData.ActuatorData("Actuator")
        
        self.ledActivator = SimpleLedActivator.SimpleLedActivator(blinkingTime)
        self.ledActivator.daemon = True
        self.ledActivator.start() 
        
        self.LedActivator = SenseHatLedActivator.SenseHatLedActivator()
        self.LedActivator.daemon = True
        self.LedActivator.start()

#     take the new data, and set the simple LED always flash. when temperature be lower, using LED display.
    def process_message(self, actuatorData):
        self.tempActuatorData.updateData(actuatorData)
        self.ledActivator.setEnableLedFlag(True)
        self.LedAction()
                
    def LedAction(self):
                
        if self.tempActuatorData.getCommand() == 0:
            message = "Temperature is lowered "
            print(message)
            self.LedActivator.setEnableLedFlag(True)
            self.LedActivator.showLEDMessage(message, 1)  
            
        if self.tempActuatorData.getCommand() == 1:
            self.LedActivator.setEnableLedFlag(False)

            message = "Temperature is high "
            print(message)
            self.LedActivator.showLEDMessage(message, 1)  
    
