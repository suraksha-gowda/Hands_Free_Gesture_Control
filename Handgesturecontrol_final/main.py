import cv2
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from hand_tracker import HandTracker
from gesture_detector import GestureDetector
from mouse_controller import MouseController

def main():
    cap = cv2.VideoCapture(0)

    tracker = HandTracker()
    detector = GestureDetector()
    mouse = MouseController()

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = tracker.find_hands(frame)
        landmarks = tracker.get_landmarks(frame)

        if landmarks:
            gesture = detector.detect_gesture(landmarks)

            if gesture:
                mouse.perform_action(gesture, landmarks)

        cv2.imshow("Hand Gesture Control", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()