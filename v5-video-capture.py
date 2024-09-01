import cv2

vid = cv2.VideoCapture(0)

frame_counter = 0

while (True):
    bool,frame=vid.read()
    cv2.imshow("bhaiiii",frame)

    key = cv2.waitKey(1) & 0xFF

    if key==ord('c'):
        filename = f"snap_{frame_counter}.png"
        cv2.imwrite(filename,frame)
        frame_counter +=1 

    elif key==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()