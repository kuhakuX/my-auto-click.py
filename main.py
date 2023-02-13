''' 
READ ME ZONE
- - - - - - - - - - I M P O R T A N T - - - - - - - - -
NEED TO INSTALL python 
NEED TO INSTALL " pillow " package --------------->  "pip install pillow"
NEED TO INSTALL " pyautogui " package --------------->  "pip install pyautogui"
NEED TO INSTALL " keyboard " package --------------->  "pip install keyboard"

- - - - - - - - - - I M P O R T A N T - - - - - - - - -
END READ ME ZONE
'''
import keyboard
import pyautogui
while keyboard.is_pressed('x')==False:
    pyautogui.click(x=34, y=38)
    pyautogui.click(x=99, y=37)
    pyautogui.click(x=196, y=38)
    pyautogui.click(x=37, y=147)
    pyautogui.click(x=196, y=138)
