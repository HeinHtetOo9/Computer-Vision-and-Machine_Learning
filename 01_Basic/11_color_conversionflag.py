import cv2 as cv

def main():
    color_flag = [i for i in dir(cv) if "COLOR_" in i]
    total = 0

    for i in color_flag:
        print(i)
        total+=1
    print("There are "+ str(total) +" number of color conversion flag")

if __name__ == '__main__':
    main()
    