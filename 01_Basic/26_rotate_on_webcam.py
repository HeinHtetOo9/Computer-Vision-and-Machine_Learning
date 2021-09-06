
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    cap = cv.VideoCapture(0)
    
    name = 'Rotate on Camera'
    cv.namedWindow(name)
    
    if cap.isOpened():
        ret,img = cap.read()
    else:
        ret = False
    row,column,ch = img.shape
    
    angle = 0
    scale = 1
    
    while True:
        ret,img = cap.read()
        
        if angle ==360:
            angle = 0
        
        R = cv.getRotationMatrix2D( (column/2,row/2), angle, scale)
        
        output = cv.warpAffine(img, R, (column,row))

        cv.imshow(name,output)
      
        time.sleep(0.001)
        angle = angle +2
        
        k = cv.waitKey(10)
        if k==27:
            break
        
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()