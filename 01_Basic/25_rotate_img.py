#python program to rotate image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.01.tiff')
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    rows,cols,channels = img.shape
    
    R = cv.getRotationMatrix2D( (cols/2,rows/2), 90,1) # 1 is for scaling
    
    print(R)
    
    output = cv.warpAffine( img, R, (cols,rows) )
    
    plt.imshow(output)
    plt.title('rotating')
    plt.show()


if __name__ == "__main__":
    main()