import cv2
img = cv2.imread('type you images path here / image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = cv2.Sobel(gray, ddept, 1,0, ksize=3, scale=1)
y = cv2.Sobel(gray, ddept, 0,1, ksize=3, scale=1)
absx= cv2.convertScaleAbs(x)
absy = cv2.convertScaleAbs(y)
edge = cv2.addWeighted(absx, 0.5, absy, 0.5,0)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
