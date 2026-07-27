import pyautogui

# Prevent pyautogui from throwing errors if the mouse reaches a screen corner
pyautogui.FAILSAFE = False


class MouseController:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()

    def perform_action(self, gesture, landmarks):
        if landmarks is None:
            return

        # Index fingertip
        x, y = landmarks[8]

        # Convert camera coordinates to screen coordinates
        screen_x = int(x * self.screen_width / 1280)
        screen_y = int(y * self.screen_height / 720)

        if gesture == "MOVE":
            pyautogui.moveTo(screen_x, screen_y)

        elif gesture == "LEFT_CLICK":
            pyautogui.click()

        elif gesture == "RIGHT_CLICK":
            pyautogui.rightClick()