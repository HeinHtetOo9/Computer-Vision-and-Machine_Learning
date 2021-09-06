import cv2 as cv
import numpy as np
import time

def emptyFunction():
    pass

def main():
    img1 = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/lake.tif')
    
    alpha = 0.0
    beta = 0.1
    gamma = 0.0
    
    output = cv.addWeighted(img1,alpha,img2,beta,gamma)
    
    win_name = "Trackbar"
    cv.namedWindow(win_name)
    
    cv.createTrackbar('Alpha',win_name,0,100,emptyFunction)
    
    while(True):
        cv.imshow(win_name,output)
        
        if cv.waitKey(1) == 27:
            break
                   
        alpha = cv.getTrackbarPos('Alpha',win_name) / 100
        beta = 1 - alpha
        
        output = cv.addWeighted(img1,alpha,img2,beta,gamma)
        
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()