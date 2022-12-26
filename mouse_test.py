import ctypes

# https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
ctypes.windll.user32.SetCursorPos(2000, 200)
ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0,0) # left down
ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0,0) # left up