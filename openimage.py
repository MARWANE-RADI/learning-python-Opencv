import cv2

img = cv2.imread("C:/Users/HP/Desktop/data/natural.jpg",-1)
img = cv2.resize(img,(500,500))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyWindow()
