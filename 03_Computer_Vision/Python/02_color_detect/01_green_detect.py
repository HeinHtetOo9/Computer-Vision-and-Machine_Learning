import cv2 as cv
import numpy as np
from numpy.core.records import get_remaining_size 


def main():
    img = cv.imread('test/01.jpg',1)
    img = cv. cvtColor(img, cv.COLOR_BGR2RGB)
    (r,g,b) = cv.split(img)
    
    r_mean = np.average(r)
    g_mean = np.average(g)
    b_mean = np.average(b)
    
    if g_mean > r_mean and g_mean > b_mean :
        print('This is Green')   
    else:
        print('This is not Green')
    
        
    while 1:
        cv.imshow("01",img)
        k = cv.waitKey(10)
        if k == 27:
            break
            
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
    