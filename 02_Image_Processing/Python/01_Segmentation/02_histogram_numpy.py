#python image processing program to show histogram with numpy
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/T.jpg',0)

    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.title('Image T')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1,2,2)
    hist,bins = np.histogram(img.ravel(),256,[0,255])
    plt.plot(hist)
    plt.title('Histogram')
    plt.xlim(xmin=0,xmax=256)
    plt.ylim([0,8000])
    plt.show()
    
if __name__ == '__main__':
    main()
    