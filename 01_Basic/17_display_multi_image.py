import cv2 as cv
import matplotlib.pyplot as plt
def main():
    img1 = cv.imread('images/lena_color_512.tif',1)
    img2 = cv.imread('images/lake.tif',1)

    plt.subplot(1,2,1)
    plt.imshow(img1)
    plt.title("Lena")

    plt.subplot(1,2,2)
    plt.imshow(img2)
    plt.title("Lake")
    
    plt.show()

if __name__ == '__main__':
    main()
    