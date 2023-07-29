import pyautogui
import time 
time.sleep(5)
for i in range(1000):
    pyautogui.typewrite("hi")
    pyautogui.press("enter")