# Walker and Adolfo Code for Red Lego Detector

import numpy as np
import cv2
import PIL.Image
from io import BytesIO
import IPython.display
import imutils
import numpy as np
from matplotlib import pyplot as plt
import serial
import time

s=serial.Serial("/dev/serial0",9600,timeout=2)



def array_to_image(a, fmt='png'):
    f = BytesIO()
    PIL.Image.fromarray(a).save(f, fmt)    
    return IPython.display.Image(data=f.getvalue())

def checkifred(picarray):
    
    lowerred = np.array([150, 0, 0])
    upperred = np.array([250, 50,50])
    mask = cv2.inRange(picarray, lowerred,upperred)
    
    return mask

d1 = IPython.display.display("Image here.", display_id=1)
frames = 0
while(True):
    cap = cv2.VideoCapture(0)
    # Capture frame-by-frame
    ret, frame = cap.read()
    cap.release()
    frames += 1
    print("\r>> Number of Frames: {}".format(frames), end='')

    # Our operations on the frame come here
    colorpic = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    array = imutils.resize(colorpic, width=200, inter=cv2.INTER_LINEAR)
    
    array = checkifred(array)
    
    #the image is now binary, sum all of the white values of the array
    
    redPixels = np.sum(array[:,:])/255
    totalPixels = array.size

    percentageRed = int((redPixels/totalPixels)*100)

    redthresh = 5
    
    if(percentageRed > redthresh):
        #This is where we communicate with the ev3 brick 
        s.write("1".encode()) #to write to EV3
        print("I SEE a RED door and I want to paint it black")

        time.sleep(1)
    else:
        
        print('NOT RED')
        time.sleep(.5)
        
    
    image = array_to_image(array)
    # Display the resulting frame
    d1.update(image)
    
    

    
