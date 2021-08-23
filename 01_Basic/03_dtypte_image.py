import cv2 as cv

def main():
    img = cv.imread("images/lena_color_512.tif",1)
    print("==========")
    print(type)
    print("==========")
    print(img.dtype)
    print("==========")
    print(img.shape)
    print("==========")
    print(img.ndim)
    print("==========")
    print(img)
    
if __name__ == "__main__":
    main()