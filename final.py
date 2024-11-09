import pyautogui
import time
import webbrowser
import pyperclip

#Move the mouse to the center of the screen
screen_width, screen_height = pyautogui.size()  # Get screen resolution
center_x, center_y = screen_width // 2, screen_height // 2  # Calculate center coordinates

# Move the mouse to the center of the screen
pyautogui.moveTo(center_x, center_y, duration=0)

#Triple-click to highlight the text
pyautogui.click()  # First 
time.sleep(0.2)    # delay
pyautogui.click()  # Second 
time.sleep(0.2)    # delay
pyautogui.click()  # Third 

#Copy the selected text (Ctrl+C)
time.sleep(0.3)  #Wait bc why not
pyautogui.hotkey('ctrl', 'c')  # Press Ctrl+C to copy the selected text

#Check if text is copied using pyperclip
time.sleep(0.8)  # Wait for the clipboard to update

# Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text
print("Copied text:", copied_text)

url = "https://create.kahoot.it/discover"

webbrowser.open_new_tab(url)


# Wait for a few seconds to switch to the window you want to interact with
time.sleep(2)

# Move the mouse to the coordinates
pyautogui.moveTo(750, 180)

# Click at the current position
pyautogui.click()

time.sleep(0.5)  #Wait bc why not
pyautogui.hotkey('ctrl', 'v')

time.sleep(0.5)  #Wait bc why not
pyautogui.hotkey('enter', 'enter')

time.sleep(2)

# Define the x and y coordinates
x11 = 350  
y11 = 500  

# Move the mouse to the coordinates over a specified duration
pyautogui.moveTo(x11, y11, duration=0.1)  # Moves

# Click at the location
pyautogui.click()

time.sleep(1.5)

# Define the x and y coordinates
x111 = 1850  
y111 = 245  

# Move the mouse to the coordinates over a specified duration
pyautogui.moveTo(x111, y111, duration=0.1)  # Moves

# Click at the location
pyautogui.click()
