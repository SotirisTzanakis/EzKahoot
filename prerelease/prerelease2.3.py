import pygetwindow as gw
import time
import pyautogui
import pyperclip
import webbrowser
from pynput.keyboard import Key, Listener

# Function to minimize VS Code
def minimize_vscode():
    try:
        vscode_window = gw.getWindowsWithTitle("Visual Studio Code")[0]  # Modify if the title changes
        vscode_window.minimize()  # Minimize the VS Code window
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

# Function definitions (same as before)
def kahoot():
    center_x, center_y = pyautogui.size()[0] // 2, pyautogui.size()[1] // 2
    pyautogui.moveTo(center_x, center_y, duration=0)
    for _ in range(3):
        pyautogui.click()
        time.sleep(0.2)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.8)
    copied_text = pyperclip.paste()
    print("Copied text:", copied_text)
    webbrowser.open_new_tab("https://create.kahoot.it/discover")
    time.sleep(2)
    pyautogui.moveTo(750, 180)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.moveTo(350, 500, duration=0.1)
    pyautogui.click()
    time.sleep(1.5)
    pyautogui.moveTo(1850, 245, duration=0.1)
    pyautogui.click()

def copyquest():
    pyautogui.moveTo(wquest, yquest)
    time.sleep(0.1)
    pyautogui.tripleClick()
    pyautogui.hotkey('ctrl', 'c')

def search():
    pyautogui.moveTo(wtb, ytb)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.press('backspace')

# Action mappings for specific keys
actions = {
    '2': lambda: pyautogui.moveTo(wyellow, yyellow),
    '1': lambda: pyautogui.moveTo(wred, yred),
    '3': lambda: pyautogui.moveTo(wblue, yblue),
    '4': lambda: pyautogui.moveTo(wgreen, ygreen),
    'c': copyquest,  # Triggers copyquest() when 'c' is pressed
    's': search,
    't': lambda: (pyautogui.moveTo(wtrue, ytrue), pyautogui.click()),  # Now t also clicks
    'k': kahoot,  # Triggers kahoot() when 'k' is pressed
    'f': lambda: (pyautogui.moveTo(wfalse, yfalse), pyautogui.click()),  # Fixed line
}

# Key press handling with toggle for repeated actions
key_state = {key: False for key in actions}

# Key press handling with toggle for repeated actions
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

# Key release handling to reset the key state, allowing the key to be pressed again
def on_release(key):
    try:
        if hasattr(key, 'char') and key.char in actions:
            key_char = key.char
            key_state[key_char] = False  # Reset the state when the key is released
    except AttributeError:
        pass  # Ignore special keys like Ctrl, Shift, etc.

# Listener setup
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
