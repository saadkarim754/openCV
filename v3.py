import cv2

path=r'me.jpeg'

img=cv2.imread(path,cv2.IMREAD_GRAYSCALE)

cv2.imwrite('new.png',img)
cv2.imshow('woooashhh here u are',img)
cv2.waitKey(0)
cv2.destroyAllWindows()