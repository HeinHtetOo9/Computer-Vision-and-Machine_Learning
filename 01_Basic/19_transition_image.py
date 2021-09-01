import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

def main():
    img1 = cv.imread('images/lena_color_512.tif',1)
    img2 = cv.imread('images/lake.tif',1)

    for i in np.linspace(0,1,100):
        alpha = i
        beta = 1-alpha
        gamma = 0
        transition_image = cv.addWeighted(img1,alpha,img2,beta,gamma)
        cv.imshow('Transition Image',transition_image)
        time.sleep(0.05)
        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
    