import pyautogui
import time

def click_mouse_every_60_seconds():
    try:
        while True:
            pyautogui.click()  # Clicks the mouse at its current location.
            time.sleep(60)  # Wait for 60 seconds before clicking again.
    except KeyboardInterrupt:
        print("Program exited.")

if __name__ == "__main__":
    click_mouse_every_60_seconds