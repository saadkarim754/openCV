import cv2
import numpy as np
import matplotlib.pyplot as plt

vid = cv2.VideoCapture(0)

mindist = 15
accuracy = 50

def circledetect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_blured = cv2.blur(gray, (3, 3))

    detected_circles = cv2.HoughCircles(gray_blured, cv2.HOUGH_GRADIENT, 1, mindist, param1=70, param2=accuracy, minRadius=1, maxRadius=40)
    
    circles = []
    if detected_circles is not None:
        detected_circles = np.uint16(np.around(detected_circles))
        for pt in detected_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]
            cv2.circle(image, (a, b), r, (0, 255, 0), 2)
            cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
            circles.append((a, b, r))
            # Draw the a, b, r values on the image
            text = f"a={a}, b={b}, r={r}"
            cv2.putText(image, text, (a - r, b - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
    
    return image, circles

# Initialize the plot
plt.ion()
fig, ax = plt.subplots()

# Example usage:
while True:
    ret, frame = vid.read()
    if not ret:
        break
    frame, circles = circledetect(frame)
    
    # Update the plot
    ax.clear()
    ax.set_xlim(0, frame.shape[1])
    ax.set_ylim(frame.shape[0], 0)
    for circle in circles:
        a, b, r = circle
        circle_plot = plt.Circle((a, b), r, color='r', fill=False)
        ax.add_artist(circle_plot)
    plt.draw()
    plt.pause(0.001)
    
    # Display the frame
    cv2.imshow("Detected Circles", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()