# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi
import time


keyList = ["\b"]
keyList.extend(iter("ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\"))

def key_check():
    return [key for key in keyList if wapi.GetAsyncKeyState(ord(key))]
 
