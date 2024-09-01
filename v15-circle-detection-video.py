import cv2 
import numpy as np

vid = cv2.VideoCapture(0)
mindist = 15
accuracy = 50

def circledetect(image):
    gray =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)   
    gray_blured = cv2.blur(gray,(3,3))

    detected_circles = cv2.HoughCircles(gray_blured, cv2.HOUGH_GRADIENT, 1, mindist, param1 = 70, param2 = accuracy, minRadius = 1, maxRadius = 40)
    if detected_circles   is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a,b,r = pt[0], pt[1], pt[2]
            cv2.circle(image, (a,b), r, (250,180,70), 2)
            cv2.circle(image, (a,b), 1, (0,0,255), 3)
    return image

while True:
    ret, frame = vid.read()
    frame = circledetect(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()