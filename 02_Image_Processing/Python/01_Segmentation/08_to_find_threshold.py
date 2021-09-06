import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/football.jpg',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    hist = cv.calcHist(img,[0],None,[256],[0,255])
    
    plt.subplot(2,1,1)
    plt.imshow(img)
    plt.title('Original')
    
    plt.subplot(2,1,2)
    plt.xlim([0,255])
    plt.plot(hist,color='g')
    plt.title('Histogram')
    
    plt.show()
    
if __name__ == '__main__':
    main()
    