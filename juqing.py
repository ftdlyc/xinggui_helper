# 自动刷剧情本

import sys

import win32gui

import game
import win32_helper
import datetime


def run(hWnd, key):
    for i in range(1):
        win32_helper.wait(3)
        win32_helper.send_key_to_window(hWnd, key)
        #game.battle(hWnd, 30)
        game.press_button_ok(hWnd)


if len(sys.argv) > 1:
    # 定时明天7点启动
    now = datetime.datetime.now()
    if int(sys.argv[1]) == 1:
        tommorow = now + datetime.timedelta(days=1, hours=31-now.hour)
    else:
        tommorow = now + datetime.timedelta(hours=7-now.hour)
    print('start time: {0}'.format(tommorow.strftime('%Y-%m-%d %H:%M:%S')))
    seconds = (tommorow - now).seconds
    win32_helper.wait(seconds)


hWnd = win32_helper.find_window_handle('MuMu', None, None)
hWnd = win32_helper.find_first_child_window(hWnd)

print("start...")

print("\nbattle 1")
run(hWnd, win32_helper.VK_A)
print("\nbattle 2")
run(hWnd, win32_helper.VK_B)
print("\nbattle 3")
run(hWnd, win32_helper.VK_C)
print("\nbattle 4")
run(hWnd, win32_helper.VK_D)

left, top, right, bottom = win32gui.GetWindowRect(hWnd)
win32_helper.send_mouse_wheel_to_window(
    hWnd, (left + right) / 2, (top + bottom) / 2, -120, 20)
win32_helper.wait(5)

print("\nbattle 5")
run(hWnd, win32_helper.VK_E)
print("\nbattle 6")
run(hWnd, win32_helper.VK_F)
print("\nbattle 7")
run(hWnd, win32_helper.VK_G)
print("\nbattle 8")
run(hWnd, win32_helper.VK_H)
print("\nbattle 9")
run(hWnd, win32_helper.VK_I)

print("\nend")
