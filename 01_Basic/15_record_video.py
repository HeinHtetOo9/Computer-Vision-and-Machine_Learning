import cv2 as cv
import matplotlib.pyplot as plt

def main():
    capture = cv.VideoCapture(0)

    window_name = "Video"
    cv.namedWindow(window_name)

    filename = "output_video.avi"
    codec =cv.VideoWriter_fourcc('X','V','I','D')
    frame_rate = 30
    resolution =(640,480)

    video_file = cv.VideoWriter(filename,codec,frame_rate,resolution)
    
    if capture.isOpened():
        ret, frame = capture.read()
    else:
        ret = False
    while(ret):
        ret, frame = capture.read()
        video_file.write(frame)
        cv.imshow("Video",frame)

        if cv.waitKey(1) == 27:
            break
    cv.destroyAllWindows()
    video_file.release()
    capture.release()

if __name__ == '__main__':
    main()