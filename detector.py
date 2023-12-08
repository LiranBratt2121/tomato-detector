import cv2
from constants import *
from distance_tracking import ObjDistanceFinder

cap = cv2.VideoCapture(0)

dist_finder = ObjDistanceFinder(real_width_cm=REAL_WIDTH_CM, width_in_frame_px=WIDTH_IN_FRAME_PX)

dist_finder.calculate_focal_length(measured_distance_cm=45)

print(f'{dist_finder.focal_length=}')

while True:
    ret, frame = cap.read()

    if frame is None:
        break
    
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    frame_threshold = cv2.inRange(
        frame_HSV, (LOW_H, LOW_S, LOW_V), (HIGH_H, HIGH_S, HIGH_V))

    
    contours, hierarchy = cv2.findContours(
        frame_threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > MIN_AREA:
            x, y, w, h = cv2.boundingRect(cnt)

            dist_finder.width_in_frame_px = w
            
            cv2.putText(frame, f'({(x,y)})', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            cv2.putText(frame, f'({(x+w,y+h)})', (w + x, h + y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            cv2.putText(frame, "Tomato", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, f'Distance: {float((dist_finder.find_distance())):.2f} cm', (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
