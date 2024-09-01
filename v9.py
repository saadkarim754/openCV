import cv2

vid = cv2.VideoCapture(0)
frame_counter=0

while (True):
    rect,frame = vid.read()

    img_bgr=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    edge=cv2.Canny(img_bgr,threshold1=30,threshold2=300)
    cv2.imshow("frame",edge)

    key = cv2.waitKey(1) & 0xFF

    if key ==ord('c'):
        cv2.imwrite('snap.png',frame)
    elif key==ord('q'):
        break


vid.release()
cv2.destroyAllWindows()