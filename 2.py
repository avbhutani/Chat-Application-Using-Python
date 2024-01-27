import ctypes
import time

# Constants for Windows API
WM_USER = 0x400
HWND_BROADCAST = 0xFFFF
WM_MY_MESSAGE = WM_USER + 1

def handle_interrupt(hwnd, msg, wparam, lparam):
    print("Interruptee: Received interrupt from Program 1")

# Register the window class
wnd_proc = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)
WndProc = wnd_proc(handle_interrupt)

class WNDCLASS(ctypes.Structure):
    _fields_ = [("lpfnWndProc", ctypes.c_void_p), ("hInstance", ctypes.c_void_p)]

wnd_class = WNDCLASS(WndProc, ctypes.windll.kernel32.GetModuleHandleW(None))
class_atom = ctypes.windll.user32.RegisterClassW(ctypes.byref(wnd_class))

# Create a window
hwnd = ctypes.windll.user32.CreateWindowExW(0, class_atom, "MessageWindow", 0, 0, 0, 0, 0, 0, 0, 0, 0)
ctypes.windll.user32.ShowWindow(hwnd, ctypes.c_int(5))

# Simulate some work
print("Interruptee: Doing some work")
time.sleep(5)

# Continue with the rest of Program 2
print("Interruptee: Continuing with its own execution")
