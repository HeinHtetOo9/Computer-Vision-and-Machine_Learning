#python program to show negative image with opencv and matplotlib
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/lake_color.tiff')

    img1 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    img3 = abs(255 - img)
    img4 = abs(255 - img)

    images = [img1,img2,img3,img4]
    titles = ['img1','img2','img3','img4']

    for image in range(len(images)):
        plt.subplot(2,2,image+1)
        plt.imshow(images[image])
        plt.title(titles[image])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()
    