# 自动铁5

import game
import win32_helper

hWnd = win32_helper.find_window_handle('MuMu', None, None)
hWnd = win32_helper.find_first_child_window(hWnd)

i = 0
while True:
    print("\nloop {0}".format(i))
    i += 1

    win32_helper.wait(3)
    win32_helper.send_key_to_window(hWnd, win32_helper.VK_X)

    game.battle(hWnd, battle_cost_times=160)
