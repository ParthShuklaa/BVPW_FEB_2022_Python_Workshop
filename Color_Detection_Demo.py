import cv2
import numpy as np
img = cv2.imread("shapes.jpg")
image= cv2.resize(img,(700,600))

#convert this image into HSV
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

#This range
lower = np.array([0,100,100])
upper = np.array([20,255,255])
mask = cv2.inRange(hsv,lower,upper)

cv2.imshow("Image",image)
cv2.imshow("Mask",mask)

cv2.waitKey(0)