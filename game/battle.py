# 2019.8.15
# by ftdlyc

import sys
sys.path.append('./')

import dip
import win32_helper
import cv2
import numpy as np
import game

def check_ap(hWnd, op_delay):
    return True

def is_win():
    return True
    

# 刷一次本
def battle(hWnd, battle_cost_times, op_delay=3, battle_end_delay=6):
    # 点击挑战
    win32_helper.wait(op_delay)
    while not game.press_button_battle_start(hWnd):
        win32_helper.wait(op_delay)

    # 吃AP药
    if not check_ap(hWnd, op_delay):
        print('ap not enough!')
        return False

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

    return True


if __name__ == "__main__":
    a = 1
    pass
