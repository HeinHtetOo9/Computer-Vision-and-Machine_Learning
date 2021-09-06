import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from numpy.lib.type_check import imag

def main():
    img = cv.imread('images/gray21.512.tiff',0)
    #img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    thresh = 100
    max_val = 255
    
    ret , out1 = cv.threshold(img,thresh,max_val,cv.THRESH_BINARY)
    ret , out2 = cv.threshold(img,thresh,max_val,cv.THRESH_BINARY_INV)
    print(out1)
    print(out2)
    
    images = [img,out1,out2]
    titles = ['img','Binary','Binary_Inv']
    
    for i in range(len(images)):
        plt.subplot(1,3,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
if __name__ == '__main__':
    main()
    