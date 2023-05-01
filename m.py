import time
import pywhatkit
from pynput import keyboard
import pandas
from pynput.keyboard import Key, Controller
import pyautogui
# def readContacts(fileName):
#     lst = []
keyboard=Controller()
def message(text: str):
    try:
        pywhatkit.sendwhatmsg_instantly(
            phone_no="+919711516723",
            wait_time=10,
            message=text,
            tab_close=False,
            close_time=5
        )
        time.sleep(5)
        pyautogui.click()
        time.sleep(5)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    except Exception:
        print("error")
message("happy birthday")