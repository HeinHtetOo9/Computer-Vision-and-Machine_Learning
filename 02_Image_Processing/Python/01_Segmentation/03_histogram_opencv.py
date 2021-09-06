#python image processing program to show histogram with opencv
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/gray21.512.tiff')
    
    hist = cv.calcHist([img],[0],None,[256],[0,255])
    
    plt.subplot(1,2,1)
    plt.imshow(img)
    plt.title('Image T')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1,2,2)
    plt.plot(hist, color ='g')
    plt.title('Histogram')
    plt.xlim(xmin=0,xmax=256)
    #plt.ylim([0,8000])
    plt.show()
    
if __name__ == '__main__':
    main()
    