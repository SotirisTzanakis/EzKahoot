import pyautogui
import time
import webbrowser
import pyperclip

wquest = 1000
yquest = 600

wtab = 80
ytab = 25

wtb = 400
ytb = 25

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

