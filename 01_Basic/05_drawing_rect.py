import cv2 as cv
import numpy as np

def main():
    img = np.zeros((512,512,3),np.uint8)
    
    cv.rectangle(img,(20,60),(160,120),(255,0,0),1)

    cv.circle(img,(160,160),40,(100,210,170),3)
    
    cv.ellipse(img,(250,250),(60,20),0,0,360,(0,255,0),-1)

    cv.imshow("Black Screen",img)

    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()