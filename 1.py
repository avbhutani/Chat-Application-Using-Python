import ctypes
import time

# Constants for Windows API
WM_USER = 0x400
HWND_BROADCAST = 0xFFFF
WM_MY_MESSAGE = WM_USER + 1

def send_interrupt(window_handle):
    ctypes.windll.user32.PostMessageW(window_handle, WM_MY_MESSAGE, 0, 0)

# Callback function for handling messages
def wnd_proc(hwnd, msg, wparam, lparam):
    print("Interrupter: Message from Program 2")
    return ctypes.windll.user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# Register the window class
class_name = "MessageWindowClass"
WNDPROC = ctypes.WINFUNCTYPE(ctypes.c_long, ctypes.c_int, ctypes.c_uint, ctypes.c_int, ctypes.c_int)
wnd_proc = WNDPROC(wnd_proc)

hinstance = ctypes.windll.kernel32.GetModuleHandleW(None)

# Define the WNDCLASS structure
wnd_class = ctypes.WNDCLASS()
wnd_class.lpfnWndProc = wnd_proc
wnd_class.hInstance = hinstance
wnd_class.lpszClassName = class_name

# Register the window class
class_atom = ctypes.windll.user32.RegisterClassW(ctypes.byref(wnd_class))

# Create a window
hwnd = ctypes.windll.user32.CreateWindowExW(0, class_atom, "MessageWindow", 0, 0, 0, 0, 0, 0, 0, hinstance, 0)
ctypes.windll.user32.ShowWindow(hwnd, ctypes.c_int(5))

# Get the handle of Program 2's window
program2_window_handle = int(input("Enter the handle of Program 2's window (in decimal): "))

# Send interrupt to Program 2 after a delay
time.sleep(2)
send_interrupt(program2_window_handle)

# Continue with the rest of Program 1
print("Interrupter: Continuing with its own execution")
