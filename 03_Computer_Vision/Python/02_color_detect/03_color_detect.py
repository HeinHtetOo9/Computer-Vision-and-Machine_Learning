import cv2 as cv
import numpy as np
from numpy.core.defchararray import array


def main():
    cap = cv.VideoCapture(0)
    
    while cap.isOpened():
        ret,frame = cap.read()
        
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        
        low_blue = np.array([100,150,150])
        high_blue=np.array([140,255,255])
        
        img_mask = cv.inRange(hsv,low_blue,high_blue)
        
        result = cv.bitwise_and(frame,frame,mask=img_mask)
        
        cv.imshow('Live',frame)
        cv.imshow('Mask',img_mask)
        cv.imshow('Result', result)
        
                
        k = cv.waitKey(33)
        if k == 27:
            break
    cv.destroyAllWindows()
    cap.release()
        
        
if __name__ == '__main__':
    main()
    