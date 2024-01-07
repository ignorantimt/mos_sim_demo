import cv2 as cv
import numpy as np

def ball_detect_demo():
    img = cv.imread('ball_image.jpg')
    cv.imshow('Original Image', img)
    cv.waitKey(0)
    gray = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
    cv.imshow('Grayscale Image', gray)
    cv.waitKey(0)
    img2 = cv.medianBlur(gray, 19)  # 进行中值模糊，去噪点
    cv.imshow('Median Blur Image', img2)
    cv.waitKey(0)
    circles = cv.HoughCircles(img2, cv.HOUGH_GRADIENT, 1, 50, param1=100, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    print(circles)

    for i in circles[0, :]:  # 遍历矩阵每一行的数据
        cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


    cv.imshow('Detected Balls',img)
    cv.waitKey(0)
    cv.destroyAllWindows()
