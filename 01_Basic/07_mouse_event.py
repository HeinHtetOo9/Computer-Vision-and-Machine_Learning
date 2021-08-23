import cv2 as cv

def main():
    events = [i for i in dir(cv) if "EVENT" in i]
    for x in events:
        print(x)

if __name__ == "__main__":
    main()