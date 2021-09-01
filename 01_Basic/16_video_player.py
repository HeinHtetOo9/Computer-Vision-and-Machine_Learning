import cv2 as cv

def main():
    name = "Video Player"
    cv.namedWindow(name)    
     
    cap = cv.VideoCapture('output_video.avi')    
  
    while cap.isOpened():
        ret,frame = cap.read()
        #clear
        # print(ret)
        if(ret):
            cv.imshow(name,frame)
            k = cv.waitKey(33) # 33 ,100
            if k == 27:
                break
        else:
            break
            
    cv.destroyAllWindows()
    cap.release()
    


if __name__ == "__main__":
    main()