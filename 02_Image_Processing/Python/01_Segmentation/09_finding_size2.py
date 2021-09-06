import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/football.jpg',0)
    
    width,height = img.shape
    total_size = width*height
    
    thresh = 200
    max_value = 1
    
    ret ,out1 = cv.threshold(img,thresh,max_value,cv.THRESH_BINARY)
    
    white_size = cv.sumElems(out1)

    print(white_size[0])
    
    images = [img,out1]
    titles = ['Original','Binary']
    
    for i in range(len(images)):      
        plt.subplot(2,3,i+1)
        plt.imshow(images[i], cmap='gray')
        plt.xticks([])
        plt.yticks([])
        plt.title(titles[i])
    plt.show()
    
    
if __name__ == '__main__':
    main()
    