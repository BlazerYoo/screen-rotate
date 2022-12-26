#https://stackify.dev/787134-python-ctypes-keyboard-event
#https://docs.microsoft.com/en-us/windows/win32/api/_inputdev/
#https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

#https://gist.github.com/Aniruddha-Tapas/1627257344780e5429b10bc92eb2f52a
#https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events

import time
import serial, ctypes
from ctypes import Structure, c_long
from key import PressKey, ReleaseKey


"""
up key: bottom bar
left key: right bar
"""
keys ={
    'up':0x26,
    'left':0x25
    }


ctrlKey = 0x11
altKey = 0x12
arduino = serial.Serial('COM5', 115200, timeout=1)


while True:

    serialOutput = arduino.readline().decode()

    # serial output is not blank
    if len(serialOutput) != 0:


        # SELECT CORRECT DISPLAY
        # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
        ctypes.windll.user32.SetCursorPos(2000, 200)
        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # left up


        # PRESS KEY SEQUENCES
        PressKey(ctrlKey)
        time.sleep(0.001)
        PressKey(altKey)
        time.sleep(0.001)

        # remove \r\n from send
        serialOutput = serialOutput[:-2]
        #print(serialOutput.lower(), keys[serialOutput.lower()])
        key = keys[serialOutput.lower()]
        PressKey(key)
        time.sleep(0.001)

        ReleaseKey(key)
        ReleaseKey(altKey)
        ReleaseKey(ctrlKey)

#arduino.close()