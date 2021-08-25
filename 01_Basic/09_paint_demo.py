import cv2 as cv
import numpy as np

drawing = False
mode = "l"
(ix,iy) = (-1,-1)

window_name = "Paint Demo"
cv.namedWindow(window_name)
img = np.zeros((1080,1920,3),np.uint8)

def draw(event,x,y,flags,param):
    global drawing,mode,ix,iy

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        (ix,iy) = x,y
        mode = "l"
    elif event == cv.EVENT_MBUTTONDOWN:
        img[img>0]=0

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == "l":
                cv.line(img,(ix,iy),(x,y),(255,255,0),1)
                (ix,iy)= x,y
                
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
    elif event == cv.EVENT_MBUTTONUP:
        drawing = False
    elif event == cv.EVENT_RBUTTONUP:
        drawing = False

cv.setMouseCallback(window_name,draw)
def main():
    global drawing,mode,ix,iy
    while True:
        cv.imshow(window_name,img)
        key = cv.waitKey(27)
        if key == 27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()