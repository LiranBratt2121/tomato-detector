import cv2
from constants import *

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if frame is None:
        break

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_threshold = cv2.inRange(frame_HSV, (LOW_H, LOW_H, LOW_V), (HIGH_H, HIGH_S, HIGH_V))

    contours, hierarchy = cv2.findContours(
        frame_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > MIN_AREA:
            x, y, w, h = cv2.boundingRect(cnt)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(30)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
