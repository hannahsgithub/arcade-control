#To be used on the RaspberryPi
#Creates a socket server that sends the signals converted from wired joystick + ADC0834 to the client as bytes
#Configure IP of client below

import socket
import RPi.GPIO as GPIO
import ADC0834
import time
from pynput.keyboard import Key, Controller

BtnPin = 22
bufferSize = 1024
ServerPort = 2000
PCip = "111.111.1.111" #Change to ip of the client/monitor/output

# Make socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as RPIsocket:
   
    # Bind socket
    # RPIsocket.bind((ServerIP, ServerPort))

    # Send start up msg
    startupMsg = "Server has started".encode('utf-8')
    RPIsocket.sendto(startupMsg, (PCip, ServerPort))
    print("Startup notice: ", startupMsg)

    # GPIO pin set up
    def setup():
        # Set the GPIO modes to BCM Numbering
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        ADC0834.setup()
   
    # Release resource
    def destroy():
        GPIO.cleanup()

    # Read joystick input then send command to client
    def loop():
        while True:
            x_val = ADC0834.getResult(0)
            y_val = ADC0834.getResult(1)
            Btn_val = GPIO.input(BtnPin)
       
        # Map joystick input to keyboard keys
            if y_val < 117: # Neutral is 127
                key_name = 'w'
            elif y_val > 137: # Neutral is 127
                key_name = 's'
            else:
                key_name = None
           
            if x_val < 121: # Neutral is 131
                key_name = 'a'
            elif x_val > 141: # Neutral is 131
                key_name = 'd'
           
            if key_name:
                cmd = key_name.encode('utf-8')
                RPIsocket.sendto(cmd, (PCip,ServerPort))
                print("Sending command:", cmd)
       
            if Btn_val == 0:
                cmd = 'f'.encode('utf-8')
                RPIsocket.sendto(cmd, (PCip,ServerPort))
                print("Sending command:", cmd)
           
            time.sleep(0.2)

    if __name__ == '__main__':
        setup()
        try:
            loop()
        except KeyboardInterrupt: # Press Ctrl C to end program
            destroy