# 自动铁5

import game
import win32_helper

op_delay = 3
battle_cost_times = 160
battle_end_delay = 6

hWnd = win32_helper.find_window_handle('MuMu', None, None)
hWnd = win32_helper.find_first_child_window(hWnd)

i = 0
while True:
    print("\nloop {0}".format(i))
    i += 1

    win32_helper.wait(op_delay)
    win32_helper.send_key_to_window(hWnd, win32_helper.VK_X)

    # 点击挑战
    win32_helper.wait(op_delay)
    while not game.press_button_battle_start(hWnd):
        win32_helper.send_key_to_window(hWnd, win32_helper.VK_X)
        win32_helper.wait(op_delay)

    # 点击略过
    win32_helper.wait(battle_cost_times)
    while not game.press_button_skip(hWnd):
        win32_helper.wait(op_delay)
        win32_helper.wait(op_delay)

    # 点击确定
    win32_helper.wait(battle_end_delay)
    while not game.press_button_ok(hWnd):
        win32_helper.wait(op_delay)
