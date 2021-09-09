import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/5.1.11.tiff',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    L1 =cv.Canny(img,30,200)
    
    L2 = cv.Canny(img, 100, 150, L2gradient=True)
    
    
    titles = ['original', 'L1 norm', 'L2 norm']
    images = [img, L1, L2]
    
    for i in range(3):
        plt.subplot(1,3,i+1)
        plt.imshow(images[i],cmap="gray")
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    
if __name__ == "__main__":
    main()
    