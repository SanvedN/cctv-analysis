from utils import load_video
import cv2
from detection import detect_objects

# loading video using the utility function
cap = load_video("root\\data\\video2.mp4")
while True:
    ret, frame = cap.read()
    output = detect_objects(frame)
    # show output frame
    cv2.imshow("output", output)
    key = cv2.waitKey(40)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
