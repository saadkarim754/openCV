import cv2
import numpy as np

img = cv2.imread('paint.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray,50,150,apertureSize=3)

lines_list=[]

lines = cv2.HoughLinesP(
            edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=100, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap between line for joining them
            )

for point in lines:
    x1, y1, x2, y2 = point[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    lines_list.append([(x1,y1),(x2,y2)])

cv2.imwrite('lines_detected.jpg',img)
cv2.imshow('image', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()
