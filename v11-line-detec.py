import cv2
import numpy as np

def detect_lines(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Perform edge detection
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    
    # Detect lines using Hough Line Transform
    lines = cv2.HoughLinesP(
        edges, # Input edge image
        1, # Distance resolution in pixels
        np.pi/180, # Angle resolution in radians
        threshold=100, # Min number of votes for valid line
        minLineLength=5, # Min allowed length of line
        maxLineGap=10 # Max allowed gap between line for joining them
    )
    
    # Draw lines on the original image
    if lines is not None:
        for point in lines:
            x1, y1, x2, y2 = point[0]
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return image

# Example usage:
img_path = 'paint.png'
img = cv2.imread(img_path)

if img is None:
    print(f"Error: Unable to read image at {img_path}")
else:
    result_img = detect_lines(img)
    cv2.imwrite('lines_detected.jpg', result_img)
    cv2.imshow('image', result_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()