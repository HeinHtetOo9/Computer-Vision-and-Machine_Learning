import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.07.tiff',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    box = cv.boxFilter(img,-1,(13,13))
    blur = cv.blur(img,(13,13))
    gaussian = cv.GaussianBlur(img,(33,33),0)
    
    
    titles = ['original','box','blur','Gaussian blur']
    images = [img,box,blur,gaussian]
    
    for i in range(len(images)):
        plt.subplot(2,2,i+1)
        plt.title(titles[i])
        plt.imshow(images[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
if __name__ == '__main__':
    main()
    