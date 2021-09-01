import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lena_color_512.tif',1)
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    
    plt.imshow(img)
    plt.show()

if __name__ == "__main__":
    main()