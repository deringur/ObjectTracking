import cv2
import numpy as np
from object_detection import ObjectDetection


cap = cv2.VideoCapture("los_angeles.mp4")

# Initialize Object Detection
od = ObjectDetection()  # Default: yolov3

while(True):

    val, frame = cap.read()

    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    idx=0
    font = cv2.FONT_HERSHEY_PLAIN  # Font of the text put above rectangle
    for box in boxes:
        detected_class_label = od.classes[class_ids[idx]]
        (x, y, w, h) = box
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, detected_class_label, (x, y+20), font, 2, (255,255,255), 2)
        idx+=1

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if (key & 0xFF) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()