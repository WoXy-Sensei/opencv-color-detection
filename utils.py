import numpy as np
import cv2 as cv


def get_limits(color:list[int]) -> tuple[np.ndarray, np.ndarray]:

    _color = np.uint8([[color]])
    hsv_color = cv.cvtColor(_color, cv.COLOR_BGR2HSV)

    h = hsv_color[0][0][0]

    lower = np.array([h - 10, 100, 100])
    upper = np.array([h + 10, 255, 255])

    return lower, upper

