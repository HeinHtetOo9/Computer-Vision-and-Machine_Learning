import cv2 as cv
import matplotlib.pyplot as plt

def main():
    capture = cv.VideoCapture(0)
    #ret, frame = capture.read()

    if capture.isOpened():
        ret, frame = capture.read()

    img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.show()
    capture.release()

if __name__ == '__main__':
    main()
    