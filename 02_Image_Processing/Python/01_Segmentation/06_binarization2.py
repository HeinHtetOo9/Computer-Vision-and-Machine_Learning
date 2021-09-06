import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/7.1.10.tiff',0)

    thresh = 0
    max_value = 255
    
    ret,out1 = cv.threshold(img,thresh,max_value,cv.THRESH_BINARY+cv.THRESH_OTSU)
    ret,out2 = cv.threshold(img,thresh,max_value,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    ret,out3 = cv.threshold(img,thresh,max_value,cv.THRESH_TOZERO+cv.THRESH_OTSU)
    ret,out4 = cv.threshold(img,thresh,max_value,cv.THRESH_TOZERO_INV+cv.THRESH_OTSU)
    ret,out5 = cv.threshold(img,thresh,max_value,cv.THRESH_TRUNC+cv.THRESH_OTSU)
    
    images = [ img , out1 , out2 , out3 , out4 , out5]    
    titles = ['Original','BINARY','BINARY_INV','TOZERO','TOZERO_INV','TURNC']
    
    for i in range(len(images)):
        plt.subplot(3,3,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()   
if __name__ == '__main__':
    main()
    