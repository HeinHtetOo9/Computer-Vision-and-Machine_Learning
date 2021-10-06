import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/crop_coins.jpg',0)
    img = cv.resize(img,None,fx = 0.35 ,fy =0.35 ,interpolation=cv.INTER_LINEAR)
    
    blk_size = 103
    constant = 2 
    
    th_img = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,blk_size,constant)
    
    medium_blur = cv.medianBlur(th_img,9)
    
    sobel_img = cv.Sobel(medium_blur,-1,1,0,ksize=13)
    canny_img = cv.Canny(medium_blur,10,250,L2gradient=True)
    lap_img = cv.Laplacian(medium_blur,-1)
    
    index,comp = cv.connectedComponents(sobel_img)
    index1,comp1 = cv.connectedComponents(canny_img)
    index2,comp2 = cv.connectedComponents(lap_img)
    
    print(index , index1 , index2)
    
    #print(comp)
    
    while True:
        cv.imshow('Canny',canny_img)
        
        k = cv.waitKey(10)
        if k == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
    