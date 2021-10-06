import cv2 as cv
import numpy as np

def main():
    img1 = cv.imread('test/01.jpg')
    img2 = cv.imread('test/02.jpg')
    img3 = cv.imread('test/03.jpg')
    img4 = cv.imread('test/04.jpg')
    img5 = cv.imread('test/05.jpg')
    img6 = cv.imread('test/06.jpg')
    img7 = cv.imread('test/07.jpg')
    img8 = cv.imread('test/08.jpg')
    img9 = cv.imread('test/09.jpg')
    
    images = [img1,img2,img3,img4,img5,img6,img7,img8,img9]
    indexs = ['01','02','03','04','05','06','07','08','09']
    texts = []
    
    for i in range(len(images)):  
        (b,g,r) = cv.split(images[i])
        r_mean = np.average(r) # np.average(img,axis=0)..
        g_mean = np.average(g)
        b_mean = np.average(b)
    
        if  ( g_mean > r_mean+20 and g_mean > b_mean+20):
            texts.append('green')
        elif( r_mean > g_mean+20 and r_mean > b_mean+20):  
            texts.append('red')
        elif( b_mean > r_mean+20 and b_mean > g_mean+20):
            texts.append('blue')
        else:
            texts.append('unknown')
            
    while 1:
        for i in range(len(images)):
            cv.imshow(indexs[i],images[i])
            cv.putText(images[i],texts[i],(100,100), cv.FONT_HERSHEY_SIMPLEX,1.2,(0,0,0))
    
        
        k = cv.waitKey(10)
        if k == 27:
            break
            

    cv.destroyAllWindows()

    
    
if __name__ == "__main__":
    main()
    
