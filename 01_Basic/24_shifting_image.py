#python program to shift an image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/4.2.01.tiff')
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    rows,cols,channels = img.shape
    
    T = np.float32([[1,0,100],[0,1,50]])
    print(T)
    
    output = cv.warpAffine(img,T,(rows,cols))
    
    plt.imshow(output)
    plt.title('Shifting')
    plt.show()


if __name__ == "__main__":
    main()