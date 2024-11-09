import pyautogui
import time

# Define the x and y coordinates
x11 = 350  # Replace with your desired x coordinate
y11 = 500  # Replace with your desired y coordinate

# Move the mouse to the coordinates over a specified duration
pyautogui.moveTo(x11, y11, duration=0.1)  # Moves over 1.5 seconds

# Click at the location
pyautogui.click()

time.sleep(1.5)

# Define the x and y coordinates
x111 = 1850  # Replace with your desired x coordinate
y111 = 245  # Replace with your desired y coordinate

# Move the mouse to the coordinates over a specified duration
pyautogui.moveTo(x111, y111, duration=0.1)  # Moves over 1.5 seconds

# Click at the location
pyautogui.click()
