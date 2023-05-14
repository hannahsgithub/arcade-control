#To be used on client
#Receives bytes from RPi that has the controls wired to,
#Outputs corresponding controls on the client that is running the video game
#Controls can be configured

import socket
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


bufferSize = 1024
ServerPort = 2000
lastKey = None

# Make socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as PCsocket:

    # Bind socket
    PCsocket.bind(("", ServerPort))

    # Waiting to receive server message
    msg, _ = PCsocket.recvfrom(bufferSize)
    print(msg.decode('utf-8'))

    # Presses key upon receiving server msg
    def send_key(key):
        global lastKey
        if key == lastKey:
            keyboard.press(key)
        else:
            if lastKey:
                keyboard.release(lastKey)
            keyboard.press(key)
            lastKey = key

    while True:
        # Waiting for server command
        time.sleep(0.2)
        data, addr = PCsocket.recvfrom(bufferSize)
        cmd = data.decode('utf-8')
        print("Inputting: ", cmd)
  
        send_key(cmd)