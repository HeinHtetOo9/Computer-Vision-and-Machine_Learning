import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = img = cv.imread('images/gray21.512.tiff',0)
    
    width,height = img.shape
    totatl_size = width*height
    print(totatl_size)
    
    thresh = 100
    max_value = 1
    
    ret,out1 = cv.threshold(img,thresh,max_value,cv.THRESH_BINARY)
    #print(out1)
    
    white_size = cv.sumElems(out1)
    
    object_size = totatl_size - white_size[0]
    print(object_size)
    
    images = [img,out1]
    titles = ['img','Binary']
    
    for i in range(len(images)):
        plt.subplot(1,2,i+1)
        plt.imshow(images[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
if __name__ == '__main__':
    main()
    