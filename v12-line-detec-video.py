import cv2
import numpy as np
vid = cv2.VideoCapture(0)


def detect_lines(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    lines = cv2.HoughLinesP(
        edges, # Input edge image
        1, # Distance resolution in pixels
        np.pi/180, # Angle resolution in radians
        threshold=190, # Min number of votes for valid line
        minLineLength=10, # Min allowed length of line
        maxLineGap=5 # Max allowed gap between line for joining them
    )
    
    # Draw lines on the original image
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(image, (x1, y1), (x2, y2), (255, 0, 255), 3)
    
    return image



frame_counter = 0

while (True):
    bool,frame=vid.read()

    lineeee=detect_lines(frame)

    cv2.imshow("bhaiiii",lineeee)

    key = cv2.waitKey(1) & 0xFF

    if key==ord('c'):
        filename = f"snap_{frame_counter}.png"
        cv2.imwrite(filename,frame)
        frame_counter +=1 

    elif key==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()