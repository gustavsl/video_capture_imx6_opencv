import numpy as np
import cv2
import time
import datetime
import sys 
import requests
import os

propertyId = '001'
siteId = '001'
upload_url = 'http://cdbws.sinactus.com/UploadArquivo'
name = propertyId + siteId + '_' + datetime.datetime.now().strftime("%Y-%m-%d_%H%M")+'.avi'

# Define the codec and create VideoWriter object
def video (seconds, frameRate):
    cap = cv2.VideoCapture("rtsp://10.22.1.199:554/user=admin&password=admin&channel=1&stream=1.sdp?")
    if(not cap.isOpened()):
        return "error"
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter(name, fourcc, frameRate, (704,480))
    # out = cv2.VideoWriter(name, 0, frameRate, (1280,720))
    nFrames=0
    print ("Starting capture...")
    while(nFrames<seconds*frameRate):
        ret, frame = cap.read()
        if ret==True:
            out.write(frame)
            nFrames += 1
        else:
            break
    print("Done. Releasing capture")
    cap.release()
    print("Wrote to file " + name + ". Bye!")

def upload():
    file_ = {'video_file': (name, open(name, 'rb'))}
    r = requests.post(upload_url, files=file_)
    print (r.text)
    print (r.status_code)
    if r.status_code == requests.codes.ok:
        os.remove(name)
        print("File "+name+" deleted!")
    else:
        print("Keeping file, transmission not ok :(")




video(10,15)
upload()
