import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.07.tiff',1)
    original = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    rgb_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    gray= cv.cvtColor(rgb_img,cv.COLOR_BGR2GRAY)
    
    ret, thresh = cv.threshold(gray,75,255,0)
    
    contours, hierarchy = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    
    cv.drawContours(rgb_img, contours, -1, (0,0,0), 2)
    
    images = [original , rgb_img]
    titles = ['Original', 'Contours']
    
    for i in range(len(images)):
        plt.subplot(1,2,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()