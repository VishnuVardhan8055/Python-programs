import cv2
img = cv2.imread('V.jpeg', 1)
print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindow()

cv2.imwrite('V_copy.png', img)
