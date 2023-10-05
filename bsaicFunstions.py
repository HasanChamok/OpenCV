import cv2 as cv

img = cv.imread('photos/3.webp')
cv.imshow("Original",img)

#convrting to grayscale
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("GRAY",gray)

#Blur an image
blur = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Detecting Cunny Edges
cunny = cv.Canny(img,125,125)
cv.imshow('Cunny Edges',cunny)

cv.waitKey(0)