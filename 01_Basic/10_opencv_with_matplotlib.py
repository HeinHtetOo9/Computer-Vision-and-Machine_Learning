import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif',0)

    plt.imshow(img , cmap='gray')
    plt.title('Lena 2')
    plt.xticks([])
    plt.yticks([])
    plt.show()
    
if __name__ == '__main__':
    main()
    