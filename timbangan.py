# test_connect.py 
import paho.mqtt.client as mqtt 
import time
import serial
from time import sleep
import re

# get data from serial
 ser = serial.Serial ("/dev/ttyUSB0", 9600)    #Open port with baud rate
while True:
    received_data = ser.read()              #read serial port
    sleep(0.03)
    data_left = ser.inWaiting()             #check for remaining byte
    received_data += ser.read(data_left)
    print (received_data)                   #print received data
    load = str(received_data)
    output = []
    repl_str = re.compile('^\d+$')
    line = load.split()
    for word in line:
            match = re.search(repl_str, word)
            if match:
                output.append(int(match.group()))
    print (output)
    load = str(output)
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected success")
        else:
            print(f"Connected fail with code {rc}")

    client = mqtt.Client() 
    client.username_pw_set(username="otochicken",password="oto")
    client.on_connect = on_connect 
    client.connect("18.119.46.225", 1883, 60) 
    # send a message to the timbangan/1/berat every 5 second
    client.publish('timbangan/1/berat', payload=load, qos=0, retain=False)
    print(f"send {load} to timbangan/1/berat")
    time.sleep(5)
    client.loop_forever()