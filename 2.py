import win32gui
import win32api
import pyautogui
import cv2




def window_enumeration_handler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))



def get_handles_from_names(names):
    current_window = win32gui.GetForegroundWindow()
    windows = []
    win32gui.EnumWindows(window_enumeration_handler, windows)
    chosen_windows = []
    for hwnd, window_name in windows:
        title = window_name.lower()
        for name in names:
            if name.lower() in title and hwnd != current_window:
                chosen_windows.append(hwnd)
                break
    return chosen_windows

def init_window(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    print(rect)
    x = rect[0]
    y = rect[1]
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    new_rect = (x,y,width,height)
    return new_rect



handles = get_handles_from_names(["check", "slack"])


for handle in handles:
    init_window(handle)

for handle in handles:
    im = pyautogui.screenshot(str(handle)+'.jpg', region=init_window(handle))