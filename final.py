import pygetwindow as gw
import time
import pyautogui
import pyperclip
import webbrowser
from pynput.keyboard import Key, Listener

    # Function to minimize VS Code
def minimize_vscode():
        try:
            vscode_window = gw.getWindowsWithTitle("Visual Studio Code")[0]
            vscode_window.minimize()
        except IndexError:
            print("VS Code window not found")

    # Call minimize function at the start
minimize_vscode()

# Mouse coordinate settings
wtrue, ytrue = 400, 800
wfalse, yfalse = 1400, 800
wred, yred = 150, 800
wblue, yblue = 1600, 800
wyellow, yyellow = 150, 960
wgreen, ygreen = 1600, 960
wquest, yquest = 1000, 600
wtb, ytb = 400, 25

#Move the mouse to the center of the screen
screen_width, screen_height = pyautogui.size()  # Get screen resolution
center_x, center_y = screen_width // 2, screen_height // 2  # Calculate center coordinates


    # Function definitions
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

        time.sleep(0.7)  #Wait bc why not
        pyautogui.hotkey('ctrl', 'v')

        time.sleep(0.7)  #Wait bc why not
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
        pyautogui.hotkey('ctrl', 'c')


def search():
        print("Executing Search function...")
        pyautogui.moveTo(wtb, ytb)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'f')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.press('backspace')
        pyautogui.click

    # Action mappings for specific keys
actions = {
        '2': lambda: pyautogui.moveTo(wyellow, yyellow),
        '1': lambda: pyautogui.moveTo(wred, yred),
        '3': lambda: pyautogui.moveTo(wblue, yblue),
        'c': copyquest,
        's': search,
        't': lambda: (pyautogui.moveTo(wtrue, ytrue), pyautogui.click()),
        'k': kahoot,
        'f': lambda: (pyautogui.moveTo(wfalse, yfalse), pyautogui.click()),
    }

    # Key press handling with toggle for repeated actions
key_state = {key: False for key in actions}

def on_press(key):
        try:
            if key == Key.esc:
                return False  # Stops the listener
            if hasattr(key, 'char') and key.char in actions:
                key_char = key.char
                if not key_state[key_char]:  # Check if the action has already been triggered
                    actions[key_char]()  # Execute the action for this key
                    key_state[key_char] = True  # Set the key as pressed (action performed)
        except AttributeError:
            pass  # Ignore special keys like Ctrl, Shift, etc.

def on_release(key):
        try:
            if hasattr(key, 'char') and key.char in actions:
                key_state[key.char] = False  # Reset the state when the key is released
        except AttributeError:
            pass  # Ignore special keys like Ctrl, Shift, etc.

    # Listener setup
with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
