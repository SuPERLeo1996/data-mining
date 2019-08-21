import cv2
import numpy as np


# 缩放
def scale(img):
    img = cv2.resize(img, None, fx=0.5, fy=0.5)
    return img


# 将读取的图像默认BGR格式转换为HSV格式
def transfer(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 70, 70])
    upper_blue = np.array([110, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask


# 腐蚀膨胀
def handle(mask):
    erode = cv2.erode(mask, None, iterations=1)
    cv2.imshow('res', erode)
    cv2.waitKey()
    dilate = cv2.dilate(erode, None, iterations=1)
    cv2.imshow('res', dilate)
    cv2.waitKey()
    return dilate


def write(path, color):
    img = cv2.imread(path)
    img = scale(img)
    rows, cols, channels = img.shape
    mask = transfer(img)
    dilate = handle(mask)
    # 遍历替换
    for i in range(rows):
        for j in range(cols):
            if dilate[i, j] == 255:
                img[i, j] = color
    cv2.imshow('res', img)
    cv2.waitKey()
    cv2.imwrite('new.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])


if __name__ == '__main__':
    path = 'glj.jpg'
    color = (0, 0, 255)
    write(path, color)
