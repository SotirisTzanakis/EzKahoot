import pyautogui
import keyboard

wred = 150
yred = 800

wblue = 1600
yblue = 800

wyellow = 150
yyellow = 960

wgreen = 1600
ygreen = 960

from pynput.keyboard import Key, Listener
import pyautogui

# Function to call when a key is pressed
def on_press(key):
    try:
        # Check if 'esc' is pressed to stop the listener
        if key == Key.esc:
            return False  # This stops the listener

        # Check if the '2' key is pressed
        elif key.char == '2':
            # Move the mouse to specified coordinates
            pyautogui.moveTo(wyellow, yyellow)
        elif key.char == '1':
            # Move the mouse to specified coordinates
            pyautogui.moveTo(wred, yred)
        elif key.char == '3':
            # Move the mouse to specified coordinates
            pyautogui.moveTo(wblue, yblue)
        elif key.char == '4':
            # Move the mouse to specified coordinates
            pyautogui.moveTo(wgreen, ygreen)

    except AttributeError:
        pass  # Ignore special keys like Ctrl, Shift, etc.

# Set up a single listener for all key events
with Listener(on_press=on_press) as listener:
    listener.join()
