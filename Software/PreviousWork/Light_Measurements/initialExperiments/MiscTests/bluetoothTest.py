#!/usr/bin/python

# This file is part of GNBot (https://github.com/carlosgs/GNBot)
# by Carlos Garcia Saura (http://carlosgs.es)
# CC-BY-SA license (http://creativecommons.org/licenses/by-sa/3.0/)

# Simple bluetooth terminal
# Based on http://stackoverflow.com/questions/15486570/bluetooth-communication-between-arduino-and-pybluez

import bluetooth
import sys

import atexit

bd_addr = "00:11:09:18:02:34" #itade address

port = 1
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print 'Connected'
sock.settimeout(0.0)
#sock.send("x")
#print 'Sent data'

def exitCallback():
    print("Closing connection...")
    sock.close()

atexit.register(exitCallback)

def BTrecv():
    try:
        data = sock.recv(1)
    except:
        return ""
    return data

while 1:
    data = BTrecv()
    written = 0
    while(len(data) > 0):
        sys.stdout.write(str(data))
        data = BTrecv()
        written += 1
    
    #if written > 0:
    #    sys.stdout.write('\n')
    
    #val = sys.stdin.readline()
    #if val == 'q\n':
    #    break
    #else:
    #    sock.send(val)

#sock.close()

