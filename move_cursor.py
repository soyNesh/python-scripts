import time
import pyautogui

while 1:
    print("Waiting...")
    mouse_pos = pyautogui.position()
    pyautogui.moveTo(mouse_pos[0] + 100, mouse_pos[1], 1)
    pyautogui.moveTo(mouse_pos[0] - 100, mouse_pos[1], 1)
    print("Cursor moved successfully!")
