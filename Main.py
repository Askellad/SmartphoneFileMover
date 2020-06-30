
import os
import win32api
import win32com.client
import socket
import Tkinter


top = Tkinter.Tk()
textWidget = Text (top, )# Code to add widgets will go here...
top.mainloop()



def isSmartphoneConnected():
    drivelist = []
    wmi = win32com.client.GetObject("winmgmts:")
    for usb in wmi.InstancesOf("Win32_PnPEntity"):
        drivelist.append(usb.Description)
    if 'Chris Handy' in drivelist or 'moto g(7) power' in drivelist:
        return True;        return False;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(('192.168.178.51', 8080))
except:
    print "fail"

sFileName = raw_input("DCIM")
sData = "Temp"

while True:
    skClient.send(sFileName)
    sData = skClient.recv(1024)
    fDownloadFile = open(sFileName, "wb")
    while sData:
        fDownloadFile.write(sData)
        sData = skClient.recv(1024)
    print "Download Completed"
    break


if not os.path.exists("A:\\"):
    print 'true'


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print drives

import socket
import sys


