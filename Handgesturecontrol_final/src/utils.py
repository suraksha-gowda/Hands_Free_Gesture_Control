import math
import time


def calculate_distance(p1, p2):
    """
    Calculate distance between two points.
    """
    return math.hypot(
        p2[0] - p1[0],
        p2[1] - p1[1]
    )


class FPSCounter:
    def __init__(self):
        self.previous_time = 0
        self.fps = 0

    def update(self):
        current_time = time.time()

        if self.previous_time != 0:
            self.fps = 1 / (current_time - self.previous_time)

        self.previous_time = current_time

        return int(self.fps)