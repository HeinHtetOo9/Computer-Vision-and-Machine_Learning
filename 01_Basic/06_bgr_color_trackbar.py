import cv2 as cv
import numpy as np

window_name = "BGR COLOR PLATTE"

cv.namedWindow(window_name)
def blue(blue):
    blue = cv.getTrackbarPos("BLUE",window_name)
    return blue
    
def green(green):
    green = cv.getTrackbarPos("GREEN",window_name)
    return green

def red(red):
    red = cv.getTrackbarPos("RED",window_name)
    return red

def main():
    img = np.zeros((512,512,3),np.uint8)

    # window_name = "BGR COLOR PLATTE"
    # cv.namedWindow(window_name)

    cv.createTrackbar("BLUE",window_name,0,255,blue)
    cv.createTrackbar("GREEN",window_name,0,255,green)
    cv.createTrackbar("RED",window_name,0,255,red)

    while True:
        cv.imshow(window_name,img)

        img[:] = [blue(blue),green(green),red(red)]
        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()

if __name__ =="__main__":
    main()