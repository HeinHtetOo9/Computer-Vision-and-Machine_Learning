import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


def main():
    img = cv.imread('images/crop_coins.jpg')
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    gray = cv.resize(gray,None,fx=0.25,fy=0.25,interpolation=cv.INTER_LINEAR)
    img = cv.resize(img,None,fx=0.25,fy=0.25,interpolation=cv.INTER_LINEAR)
    
    blk_size= 101
    constant = 2
    
    th_img = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,101,2)
    
    smooth_img = cv.medianBlur(th_img,3)
    
    canny_img = cv.Canny(smooth_img,100,100,L2gradient=True)
    
    cv.imshow("Canny_edge_detect",canny_img)
    
    counts, hireachy = cv.findContours(canny_img.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    
    print("Total Coins = {}".format( len(counts) ) )
    contour = img.copy()
    cv.drawContours(contour, counts, -1, (0,0,255), 2)
    cv.imshow("Coins", contour)
    k = cv.waitKey(0)
    if k == 27:
        cv.destroyAllWindows()
if __name__ == '__main__':
    main()
    