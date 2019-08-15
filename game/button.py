# 2019.8.14
# by ftdlyc

import sys
sys.path.append('./')

import numpy as np
import cv2
import win32_helper
import dip
from game.base import *


k_button_path = {
    'skip': './pic/button_skip.png',
    'ok': './pic/button_ok.png',
    'battle_start': './pic/button_battle_start.png'
}

k_button_img = {}


def press_button_aux(hWnd, name, thr = 0.8):
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    template = k_button_img[name]
    ret, val = press_button(hWnd, template, thr)
    if ret:
        print('press button {0}, val = {1}'.format(name, val))
    else:
        print('no find button {0}, val = {1}'.format(name, val))
    return ret


# 点击略过
def press_button_skip(hWnd):
    return press_button_aux(hWnd, 'skip')


# 点击确定
def press_button_ok(hWnd):
    return press_button_aux(hWnd, 'ok')


# 点击挑战
def press_button_battle_start(hWnd):
    return press_button_aux(hWnd, 'battle_start')


if __name__ == "__main__":
    handle = win32_helper.find_window_handle('MuMu', None, None)
    handle = win32_helper.find_first_child_window(handle)
    press_button_ok(handle)
    pass
