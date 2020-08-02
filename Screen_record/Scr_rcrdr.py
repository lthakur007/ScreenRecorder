# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:51:27 2020

@author: lthakur
"""


import cv2
import numpy as np
import pyautogui
import time

pyautogui.size()
# display screen resolution, get it from your OS settings
SCREEN_SIZE = pyautogui.size()
print(SCREEN_SIZE)
# define the codec
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
fourcc = cv2.VideoWriter_fourcc(*"MP4V")
# create the video write object
out = cv2.VideoWriter("small_change.mp4", fourcc, 20.0, (1920,1000))
color = (0, 0, 0)
radius=5
time.sleep(5)
start = time.time()

while True:
    # make a screenshot
    img = pyautogui.screenshot(region=(50,50,1920,1000))
    #x,y = pyautogui.position()
    #area = np.array([[x,y],[(x+20),(y+20)]])
    # convert these pixels to a proper numpy array to work with OpenCV
    frame = np.array(img)
    # convert colors from BGR to RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #cv2.fillPoly(frame,[area],color=[0,0,0])
    #frame=cv2.circle(frame, (x,y), radius, color,-1)
    # write the frame
    out.write(frame)
    stop = time.time()
    print(time.time() - start)
    if  (time.time() - start) > 20 :
        break
    # show the frame
    #cv2.imshow("screenshot", frame)
    # if the user clicks q, it exits
    #if cv2.waitKey(1) == ord("q"):
    #    break

# make sure everything is closed when exited
#cv2.destroyAllWindows()
out.release()