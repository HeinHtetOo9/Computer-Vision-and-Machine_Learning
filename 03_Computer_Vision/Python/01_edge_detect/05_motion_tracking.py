import cv2 as cv
import numpy as np

def main():
    width = 980
    height = 640
    
    cap = cv.VideoCapture(0)
    
    # cv.set(3,width)
    # cv.set(4,height)
    
    if cap.isOpened():
        ret,frame1 = cap.read()
        ret,frame2 = cap.read()
        
    else:
        ret = False
        
    while ret:
        
        frame_diff = cv.absdiff(frame1,frame2)
        
        gray_frame = cv.cvtColor(frame_diff,cv.COLOR_BGR2GRAY)
        
        blur = cv.GaussianBlur(gray_frame,(5,5),0)
        
        ret ,th = cv.threshold(blur,50,255,cv.THRESH_BINARY)
        
        dilated = cv.dilate(th,np.ones((3,3),np.uint8),iterations=3)
        
        eroded = cv.erode( th, np.ones((3,3),np.uint8), iterations = 5 )
        
        # c,h = cv.findContours(dilated,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        # c,h = cv.findContours(eroded,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        
        # cv.drawContours(frame1,c,-1,(0,255,0),2)
        
        cv.imshow('Original',frame2)
        cv.imshow('Motion',dilated)
                
        
        if cv.waitKey(1)==27:
            break
               
        frame1 = frame2
        ret,frame2 = cap.read()
        
    cv.destroyAllWindows()
    cap.release()
    
if __name__ == '__main__':
    main()
    