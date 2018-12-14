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
name = propertyId + siteId + '_' + \
    datetime.datetime.now().strftime("%Y-%m-%d_%H%M")+'.jpg'

# Define the codec and create VideoWriter object


def video(seconds, frameRate):
    cap = cv2.VideoCapture("rtsp://10.22.1.199:554/user=admin&password=admin&channel=1&stream=0.sdp?")
    if(not cap.isOpened()):
        return "error"
    print("Starting capture...")
    ret, frame = cap.read()
    cv2.imwrite(name, frame)
    print("Done. Releasing capture")
    cap.release()
    print("Wrote to file " + name + ". Bye!")


def upload():
    file_ = {'video_file': (name, open(name, 'rb'))}
    r = requests.post(upload_url, files=file_)
    print(r.text)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        os.remove(name)
        print("File "+name+" deleted!")
    else:
        print("Keeping file, transmission not ok :(")


video(5, 15)
upload()
