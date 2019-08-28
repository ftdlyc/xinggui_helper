# 2019.8.15
# by ftdlyc

import sys
sys.path.append('./')

import cv2
import numpy as np

import dip
import game
import win32_helper



def check_ap(hWnd, op_delay, n):
    if game.has_select_box(hWnd):
        # 点击确定
        while not game.press_button_ok(hWnd):
            win32_helper.wait(op_delay)

        # 吃4次AP药
        nsucceed = 0
        for i in range(n):
            if not game.press_button_use_ap(hWnd):
                break

            while not game.has_select_box(hWnd):
                game.press_button_use_ap(hWnd)
                win32_helper.wait(op_delay)

            while not game.press_button_ok(hWnd):
                win32_helper.wait(op_delay)

            nsucceed = nsucceed + 1

        # 点击交叉
        while not game.press_button_cross(hWnd):
            win32_helper.wait(op_delay)

        return nsucceed
    else:
        return -1


def is_win():
    return True


# 刷一次本
def battle(hWnd, battle_cost_times, op_delay=3, battle_end_delay=6):
    # 点击挑战
    win32_helper.wait(op_delay)
    while not game.press_button_battle_start(hWnd, False):
        win32_helper.wait(battle_end_delay)

    # 吃4次AP药
    n = check_ap(hWnd, op_delay=op_delay, n=1)
    if n == 0:
        print('ap not enough!')
        return False
    elif n > 0:
        print('use ap {0} times'.format(n))
        return battle(hWnd, battle_cost_times, op_delay, battle_end_delay)
    win32_helper.wait(op_delay)

    # 等待战斗结束
    win32_helper.wait(battle_cost_times)

    # 判断是否失败
    if not is_win():
        win32_helper.wait(battle_end_delay)
        print('lost the battle!')
        return True

    # 点击略过
    while not game.press_button_skip(hWnd):
        win32_helper.wait(op_delay)
        win32_helper.wait(op_delay)

    # 点击确认
    win32_helper.wait(battle_end_delay)
    while not game.press_button_reward_check(hWnd):
        win32_helper.wait(op_delay)

        # 若没有奖励, 跳出
        if game.has_mainui_sign(hWnd):
            print('No reward')
            break

    return True


if __name__ == "__main__":
    handle = win32_helper.find_window_handle('MuMu', None, None)
    handle = win32_helper.find_first_child_window(handle)
    battle(handle, 10000)
    pass
