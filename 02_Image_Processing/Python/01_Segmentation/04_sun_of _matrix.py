import cv2 as cv

def main():
    img = cv.imread('images/T.jpg',0)
    
    sum = cv.sumElems(img)
    
    print(sum)
    
if __name__ == '__main__':
    main()
    