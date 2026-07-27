from utils import calculate_distance


class GestureDetector:

    def __init__(self):
        pass

    def detect_gesture(self, landmarks):

        if landmarks is None or len(landmarks) < 21:
            return None

        # Hand landmarks
        thumb_tip = landmarks[4]
        index_tip = landmarks[8]
        middle_tip = landmarks[12]

        # Distance between thumb and index finger
        pinch_distance = calculate_distance(
            thumb_tip,
            index_tip
        )

        # Left click gesture
        if pinch_distance < 40:
            return "LEFT_CLICK"

        # Right click gesture
        middle_distance = calculate_distance(
            index_tip,
            middle_tip
        )

        if middle_distance < 30:
            return "RIGHT_CLICK"

        # Default gesture
        return "MOVE"