import cv2 as cv
import numpy as np

window_name = "Click to Circle"
cv.namedWindow(window_name)
img = np.zeros((512,512,3),np.uint8)

def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),40,(100,210,170),3)
    elif event == cv. EVENT_MBUTTONDBLCLK:
        cv.circle(img,(x,y),30,(255,0,0),-1)

cv.setMouseCallback(window_name,draw_circle)
def main():
    while True:
        cv.imshow(window_name,img)
        if cv.waitKey(27)==27:
            break
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()