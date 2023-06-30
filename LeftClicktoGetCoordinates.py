# Handle Mouse Events in OpenCV
import numpy as np
import cv2

img = np.zeros([512,512,3],np.uint8)
# img = cv2.imread('sunflower.jpeg')
cv2.imshow('image',img)
# window name 'image' should be same everywhere

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #left click prints coordinates of that point
        print(x,', ',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(x) + ', '+str(y)
        cv2.putText(img,text,(x,y),font,0.5,(255,255,0),2)
        cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()