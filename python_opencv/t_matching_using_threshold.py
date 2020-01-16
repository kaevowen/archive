import cv2 as cv
import numpy as np

img_rgb = cv.imread('image/12.bmp')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('1.png', 0)
w, h = template.shape[::-1]
count = 0

res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)

threshold = 0.9
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    count+=1

cv.imshow('result', img_rgb)
cv.waitKey(0)

print('count : ', count)