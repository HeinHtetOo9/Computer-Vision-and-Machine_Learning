import cv2 as cv
import matplotlib.pyplot as plt

def main():
    img = cv.imread('images/5.1.11.tiff',1)
    img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    
    # change kernel size
    lap = cv.Laplacian(img,-1,ksize=11, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)
    # soble
    v_sob = cv.Sobel( img, -1, dx=1, dy=0, ksize=11, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)#change dx
    h_sob = cv.Sobel( img, -1, dx=0, dy=1, ksize=11, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)#change dy
    sob   = v_sob + h_sob
    # sharr
    v_sha = cv.Scharr( img, -1, dx=1, dy=0, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)#change dx
    h_sha = cv.Scharr( img, -1, dx=0, dy=1, scale=1, delta=0, borderType=cv.BORDER_DEFAULT)#change dy
    sharr = v_sha + h_sha
    
    images = [img, lap, v_sob, h_sob, sob, v_sha, h_sha, sharr]
    titles = ['Original', 'Laplacian', 'dx=1 dy=0', 'dx=0 dy=1', 'Sobel', 'v_sha', 'h_sha', 'sharr']
    
    for i in range(8):
        plt.subplot(3,3,i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
    
if __name__ == "__main__":
    main()