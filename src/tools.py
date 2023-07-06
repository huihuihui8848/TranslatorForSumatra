import win32gui


def get_active_window_class():
    try:
        hwnd = win32gui.GetForegroundWindow()
        return win32gui.GetClassName(hwnd)
    except:
        return '-1'
