import cv2 as cv
import numpy as np

def main():
    img = np.zeros((512,512,3),np.uint8)
    
    #cv.rectangle(img,(x,y),(x1,y1),(blue,green,red),thickness)
    cv.rectangle(img,(20,60),(60,120),(255,0,0),1)

    #cv.circle(img,(start_points),radius,(color),thickness)
    cv.circle(img,(160,160),40,(100,210,170),3)
    
    #cv.ellipse(img,(start_points),(two_radius),rotation,0 to 360,(color),thickness)
    cv.ellipse(img,(250,250),(60,20),0,0,360,(0,255,0),-1)

    cv.imshow("Black Screen",img)

    cv.waitKey(0)
    cv.destroyAllWindows()
if __name__ == "__main__":
    main()