import cvlib as cv
from cvlib.object_detection import draw_bbox
import cv2


# using cvlib we draw box around objects
def detect_objects(frame):
    bbox, label, conf = cv.detect_common_objects(frame)
    frame = draw_bbox(frame, bbox, label, conf)
    cv2.putText(
        frame,
        str(label.count("person")),
        (50, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        2,
        (255, 0, 0),
        3,
    )
    return frame
