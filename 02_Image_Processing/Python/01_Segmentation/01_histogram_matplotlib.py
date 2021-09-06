#python image processing program to show histogram with matplotlib
import cv2 as cv
import matplotlib.pyplot as plt


def main():
    img = cv.imread('images/T.jpg', 0)

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])

    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()


if __name__ == "__main__":
    main()
    