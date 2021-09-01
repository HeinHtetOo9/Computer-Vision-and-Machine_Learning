import cv2 as cv
import matplotlib.pyplot as plt

def main():
    capture = cv.VideoCapture(0)
    #ret, frame = capture.read()
    capture.set(3,1024)
    capture.set(4,768)
    if capture.isOpened():
        ret, frame = capture.read()
    else:
        ret = False
    while(ret):
        ret, frame = capture.read()
        cv.imshow("Video",frame)

        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()
    capture.release()


if __name__ == '__main__':
    main()