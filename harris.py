import cv2
import numpy as np

filename = '3.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2HLS_FULL)
gray = np.float32(gray)
dst = cv2.dilate(gray, None)
img[dst > 0.01*dst.max()] = [0, 0, 255]
# dst = cv2.cornerHarris(gray, 2, 3, 0.04)
cv2.imshow(img)
cv2.waitKey()