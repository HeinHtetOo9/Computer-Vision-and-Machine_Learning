#python program to show logical operation of image 
import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img1 = cv.imread('images/lena_color_512.tif')
    img2 = cv.imread('images/lake_color.tiff')

    img1 = cv.cvtColor(img1,cv.COLOR_BGR2RGB)
    img2 = cv.cvtColor(img2,cv.COLOR_BGR2RGB)

    img_not = cv.bitwise_not(img1)
    img_and = cv.bitwise_and(img1,img2)
    img_or = cv.bitwise_or(img1,img2)
    img_xor =cv.bitwise_xor(img1,img2)

    images = [img1,img2,img_not,img_and,img_or,img_xor]
    titles = ['img1','img2','img_not','img_and','img_or','img_xor']

    for image in range(len(images)):
        plt.subplot(3,3,image+1)
        plt.imshow(images[image])
        plt.title(titles[image])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == '__main__':
    main()
    