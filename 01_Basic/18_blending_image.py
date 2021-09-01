import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img1 = cv.imread('images/lena_color_512.tif',1)
    img2 = cv.imread('images/lake.tif',1)

    alpha = 0.4  #alpha + beta must be 1"
    beta = 0.6
    gamma = 0

    blending_image = cv.addWeighted(img1,alpha,img2,beta,gamma)

    plt.imshow(blending_image)
    plt.show()

if __name__ == '__main__':
    main()
    