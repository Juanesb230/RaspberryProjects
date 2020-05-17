import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

GPIO.setmode(GPIO.BCM)
HEX_Directions = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE3], [0xF0, 0xF0, 0xF0, 0xF0, 0xE3]]
rpiAntenna = NRF24(GPIO, spidev.SpiDev())
rpiAntenna.begin(0, 17)
 
rpiAntenna.setPayloadSize(32)
rpiAntenna.setChannel(0x76)
rpiAntenna.setDataRate(NRF24.BR_1MBPS)
rpiAntenna.setPALevel(NRF24.PA_MAX)
rpiAntenna.setAutoAck(True)
rpiAntenna.enableDynamicPayloads()
rpiAntenna.enableAckPayload()
rpiAntenna.openWritingPipe(HEX_Directions[0])
rpiAntenna.openReadingPipe(1, HEX_Directions[1])
rpiAntenna.printDetails()

rpiMessage = list("GETSTRING")
while len(rpiMessage) < 32:
    rpiMessage.append(0)
 
start = time.time()
rpiAntenna.write(rpiMessage)
print("Sent the message: {}".format(rpiMessage))
rpiAntenna.startListening()
 
while not rpiAntenna.available(0):
   time.sleep(1 / 100)
   if time.time() - start > 5:
     print("Timed out.")
     break

receivedArduinoMessage = []
rpiAntenna.read(receivedArduinoMessage, rpiAntenna.getDynamicPayloadSize())
print("Received: {}".format(receivedArduinoMessage)) 
decodeArduinoMessage = ""
for n in receivedArduinoMessage:
    if (n >= 48 and n <= 57 or n==46):
        decodeArduinoMessage += chr(n)
print("Arduino message decodes to: {}".format(decodeArduinoMessage))
rpiAntenna.stopListening()


