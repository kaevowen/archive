import psutil
import win32gui
import win32process

PROCNAME = "exefile.exe"


def get_processes(Pname):
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            yield proc


def get_hwnds(pid):
    """return a list of window handlers based on it process id"""
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


def get_window_text(pyhandle):
    return win32gui.GetWindowText(pyhandle)