import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.04.tiff',0)
    
    out1 = cv.equalizeHist(img)
    
    #clache = cv.createCLAHE()
    clache = cv.createCLAHE(clipLimit=1.0,tileGridSize=(8,8))
    out2 = clache.apply(img)
    
    images = [img, out1, out2]
    titles = ['Original', 'Adjusted Histogram','CLAHE']
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.hist(images[i].ravel(),256,[0,255])
        plt.title(titles[i])
    plt.show()

if __name__ == "__main__":
    main()