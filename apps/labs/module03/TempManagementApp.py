from labs.module03 import TempSensorAdaptor
from labs.common import ActuatorData
from time import sleep
from labs.module03 import TempActuatorEmulator


path = "../../../data/ConnectedDevicesConfig.props"
# new TempSensorAdaptor constructor 
tempSensor = TempSensorAdaptor.TempSensorAdaptor(25, 15, 4, 1, path)
tempSensor.daemon = True
tempActuatorData = ActuatorData.ActuatorData("Actuator")

tempActuatorEmulator = TempActuatorEmulator.TempActuatorEmulator(5)
# start thread to get current temperature
tempSensor.start()
while True:
#     change the LED mode, because of the changing of temperature
    if tempSensor.curTemp > int(tempSensor.nominalTemp ):
        tempActuatorData.setCommand(1)
    if tempSensor.curTemp < int(tempSensor.nominalTemp):
        tempActuatorData.setCommand(0)
            
    tempActuatorEmulator.process_message(tempActuatorData)
    sleep(5)
