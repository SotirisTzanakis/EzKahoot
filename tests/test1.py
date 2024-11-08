import pyautogui
import time
import pyperclip

# Step 1: Move the mouse to the center of the screen
time.sleep(0.5)
screen_width, screen_height = pyautogui.size()  # Get screen resolution
center_x, center_y = screen_width // 2, screen_height // 2  # Calculate center coordinates

# Move the mouse to the center of the screen
pyautogui.moveTo(center_x, center_y, duration=1)

# Step 2: Triple-click to highlight the text (triple-clicking is done by clicking 3 times)
pyautogui.click()  # First click
time.sleep(0.2)    # Short delay between clicks
pyautogui.click()  # Second click
time.sleep(0.2)    # Short delay between clicks
pyautogui.click()  # Third click

# Step 3: Copy the selected text (simulate Ctrl+C)
time.sleep(0.5)  # Give it a moment for the triple-click to highlight the text
pyautogui.hotkey('ctrl', 'c')  # Press Ctrl+C to copy the selected text

# Step 4: Check if text is copied using pyperclip
time.sleep(1)  # Wait for the clipboard to update

# Get the copied text from the clipboard
copied_text = pyperclip.paste()

# Print the copied text
print("Copied text:", copied_text)
