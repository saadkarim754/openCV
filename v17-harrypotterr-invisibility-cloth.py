import cv2 # type: ignore
import numpy as np 
import time

def per_image_effect_creator(img, background):
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1 = np.array([100, 40, 40])
    upper_red1 = np.array([100, 255, 255])
    lower_red2 = np.array([155, 40, 40])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=3)
    mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=2)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    return final_output

def main():
    capture_video = cv2.VideoCapture(0)
    time.sleep(1)
    for i in range(60):
        return_val, background = capture_video.read()
        if not return_val:
            continue
    background = np.flip(background, axis=1)
    while capture_video.isOpened():
        return_val, img = capture_video.read()
        if not return_val:
            break
        final_output = per_image_effect_creator(img, background)
        cv2.imshow("INVISIBLE MAN", final_output)
        if cv2.waitKey(10) == ord('q'):
            break
    capture_video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()