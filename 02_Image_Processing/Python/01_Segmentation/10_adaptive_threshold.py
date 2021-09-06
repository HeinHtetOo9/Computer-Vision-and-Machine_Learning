import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def main():
    img = cv.imread('images/4.1.05.tiff',0)
    
    block_size = 215
    constant = 4
    
    th1 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, block_size, constant )
    th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, block_size, constant )
    
    images = [img, th1, th2]
    titles = ['Original','Mean', 'Gaussian']
    
    for i in range(len(images)):      
        plt.subplot(1,3,i+1)
        plt.imshow(images[i], cmap="gray")
        plt.xticks([])
        plt.yticks([])
        plt.title(titles[i])
    plt.show()

if __name__ == "__main__":
    main()