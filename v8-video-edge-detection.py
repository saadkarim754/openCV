import cv2

vid = cv2.VideoCapture(0)

frame_counter = 0

while (True):
    bool,frame=vid.read()

    img_BGR = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)   
    edges = cv2.Canny(image=img_BGR,threshold1= 50,threshold2=400)
    cv2.imshow("bhaiiii",edges)

    key = cv2.waitKey(1) & 0xFF

    if key==ord('c'):
        filename = f"snap_{frame_counter}.png"
        cv2.imwrite(filename,frame)
        frame_counter +=1 

    elif key==ord('q'):
        break

vid.release()
cv2.destroyAllWindows()