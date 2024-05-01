import cv2 as cv
from utils import get_limits
from PIL import Image

camera_id = 0 # Change this value if you have multiple cameras
color = [0, 255, 0]  # BGR format
box_color = (255, 0, 0)  # BGR format
box_thickness = 2


def main() -> None:
    ret = True
    webcam = cv.VideoCapture(camera_id)
    while ret:
        ret, frame = webcam.read()

        if not ret:
            break

        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lowerLimit, upperLimit = get_limits(color)
        mask = cv.inRange(hsv_frame, lowerLimit, upperLimit)
        mask_array = Image.fromarray(mask)
        bbox = mask_array.getbbox()

        if bbox:
            cv.rectangle(frame, (bbox[0], bbox[1]),(bbox[2], bbox[3]), box_color, box_thickness)

        cv.imshow('Webcam', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()