#python opencv program to show split and merge with matplotlib
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.01.tiff',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)

    r,g,b = cv.split(img)

    images = [cv.merge((r,g,b)),r,g,b]
    titles = ["Merge_image","Red","Green","Blue"]

    for i in range(len(images)):
        plt.subplot(2,2,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()
    