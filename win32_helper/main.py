# 2019.8.14
# by ftdlyc

import time
import os
import sys
import win32api
import win32con
import win32gui
import win32process

kSearchTime = 5

# 等待(秒)
def wait(ts):
    time.sleep(ts)


# 寻找标题为title,父窗口为parent_hWnd的顶级窗口的句柄
# parent_hWnd可以为None
# func为自定义判断函数,调用为func(hWnd, *args),可以为None
def find_window_handle(title, parent_hWnd, func, *args):
    target_hWnd = None
    hWnd_list = []
    clk = time.time()
    while True:
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWnd_list)
        for hWnd in hWnd_list:
            if win32gui.GetWindowText(hWnd).find(title) != -1 \
                    and (not parent_hWnd or win32gui.GetParent(hWnd) == parent_hWnd) \
                    and (not func or func(hWnd, *args)):
                target_hWnd = hWnd
                break
        if target_hWnd or kSearchTime < time.time() - clk:
            break
        hWnd_list.clear()
    return target_hWnd


# 返回第一个子窗口
def find_first_child_window(hWnd):
    return win32gui.FindWindowEx(hWnd, None, None, None)


# 向类名为wnd_class,标题为wnd_text的子窗口发送消息
# msg为windows消息,msg为list是可以发送多条消息
def send_messages_to_child_window(parent_hWnd, wnd_class, wnd_text, msgs, wParams, lParams):
    child_hWnd = win32gui.FindWindowEx(parent_hWnd, None, wnd_class, None)
    while child_hWnd:
        if not wnd_text or win32gui.GetWindowText(child_hWnd).find(wnd_text) != -1:
            if type(msgs) is list:
                for msg, wParam, lParam in zip(msgs, wParams, lParams):
                    win32gui.SendMessage(child_hWnd, msg, wParam, lParam)
            else:
                win32gui.SendMessage(child_hWnd, msgs, wParams, lParams)
            break
        child_hWnd = win32gui.FindWindowEx(parent_hWnd, child_hWnd, wnd_class, None)
    return child_hWnd


# 向指定窗口发送按键
def send_key_to_window(hWnd, key):
    win32gui.SendMessage(hWnd, win32con.WM_KEYDOWN, key, 0)
    wait(0.01)
    win32gui.SendMessage(hWnd, win32con.WM_KEYUP, key, 0)


def in_pid_list(hWnd, *args):
    pid_list = args[0]
    for pid in pid_list:
        if pid in win32process.GetWindowThreadProcessId(hWnd):
            return True
    return False
