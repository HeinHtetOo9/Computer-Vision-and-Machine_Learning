import cv2 as cv
import numpy as np

def main():
    img = np.zeros((512,512,3),np.uint8)
    
    cv.line(img,(100,100),(200,250),(100,200,100),2)

    cv.imshow("Black Screen",img)

    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()