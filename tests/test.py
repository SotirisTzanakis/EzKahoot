
import pyautogui
import time
import webbrowser

url = "https://create.kahoot.it/discover"

webbrowser.open_new_tab(url)


# Wait for a few seconds to switch to the window you want to interact with
time.sleep(2)

# Move the mouse to the coordinates (750, 90)
pyautogui.moveTo(750, 180)

# Click at the current position
pyautogui.click()
