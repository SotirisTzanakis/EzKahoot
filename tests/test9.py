import pyautogui
import time
import webbrowser
import pyperclip
import keyboard

wtrue = 400
ytrue = 800

wfalse = 1400
yfalse = 800

wred = 150
yred = 800

wblue = 1600
yblue = 800

wyellow = 150
yyellow = 960

wgreen = 1600
ygreen = 960

wquest = 1000
yquest = 600

wtab = 80
ytab = 25

wtb = 400
ytb = 25

#Move the mouse to the center of the screen
screen_width, screen_height = pyautogui.size()  # Get screen resolution
center_x, center_y = screen_width // 2, screen_height // 2  # Calculate center coordinates

# Move the mouse to the center of the screen
def kahoot():
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


def copyquest():
    pyautogui.moveTo(wquest, yquest)
    time.sleep(0.1)
    pyautogui.tripleClick()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'c')

def search():
    pyautogui.moveTo(wtb, ytb)
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'f')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

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
        elif key.char == 'c':
            # Move the mouse to specified coordinates
            copyquest()
        elif key.char == 's':
            # Move the mouse to specified coordinates
            search()
        elif key.char == 't':
            # Move the mouse to specified coordinates
            pyautogui.moveTo(wgreen, ygreen)
        elif key.char == 'k':
            # Move the mouse to specified coordinates
            kahoot()

    except AttributeError:
        pass  # Ignore special keys like Ctrl, Shift, etc.

# Set up a single listener for all key events
with Listener(on_press=on_press) as listener:
    listener.join()




