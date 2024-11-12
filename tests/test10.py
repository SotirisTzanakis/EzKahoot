import time
import pyautogui
import pyperclip
import webbrowser
from pynput.keyboard import Key, Listener

# Mouse coordinate settings
wtrue, ytrue = 400, 800
wfalse, yfalse = 1400, 800
wred, yred = 150, 800
wblue, yblue = 1600, 800
wyellow, yyellow = 150, 960
wgreen, ygreen = 1600, 960
wquest, yquest = 1000, 600
wtb, ytb = 400, 25

# Function definitions
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
    't': lambda: pyautogui.moveTo(wtrue, yfalse),
    'k': kahoot,  # Triggers kahoot() when 'k' is pressed
    'f': lambda: pyautogui.moveTo(wfalse, yfalse)
}

# Key press handling
def on_press(key):
    try:
        if key == Key.esc:
            return False  # Stops the listener
        elif hasattr(key, 'char') and key.char in actions:
            actions[key.char]()  # Executes the corresponding action
    except AttributeError:
        pass  # Ignore special keys like Ctrl, Shift, etc.

# Listener setup
with Listener(on_press=on_press) as listener:
    listener.join()
