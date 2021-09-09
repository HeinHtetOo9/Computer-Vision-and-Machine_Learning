import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    img = cv.imread('images/lena_color_512.tif',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    rows,columns,channels = img.shape
    p = 0.05

    output = np.zeros(img.shape,np.uint8)
    
    for i in range(rows):
        for j in range(columns):
            r = random.random() # float between 0 and 1
            if r < p/2:
                # pepper sprinkled
                output[i][j] = [0,0,0]
            elif r < p:
                # salt sprinkled
                output[i][j] = [255,255,255]
            else:
                output[i][j] = img[i][j]
    
    denoised = cv.medianBlur(output,3)
    blur = cv.GaussianBlur(img,(5,5),0)
    
    plt.subplot(1,3,1)
    plt.imshow(output)
    plt.title('Image with salt and noise')
    
    plt.subplot(1,3,2)
    plt.imshow(denoised)
    plt.title('median blur filter')
    
    plt.subplot(1,3,3)
    plt.imshow(blur)
    plt.title('GaussianBlur')
    
    plt.show()
        
            
if __name__ == '__main__':
    main()
    