import cv2

#Reading an Image using OPen CV
img = cv2.imread('Images\Feedingdogs.jpg')
cv2.imshow('image',img)

#For Holding the Screen until User presses a Key
cv2.waitKey(0)

#Destroying all Windows on screen
cv2.destroyAllWindows()