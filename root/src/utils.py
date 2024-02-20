import cv2


# utility function to load a video specified its path
def load_video(path):
    cap = cv2.VideoCapture(path)
    return cap