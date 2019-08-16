# 2019.8.14
# by ftdlyc

import sys
sys.path.append('./')

import cv2
import numpy as np
import win32gui

import dip
import win32_helper


k_button_path = {
    'skip': './pic/button_skip.png',
    'ok': './pic/button_ok.png',
    'cancel': './pic/button_cancel.png',
    'battle_start': './pic/button_battle_start.png',
    'reward_check': './pic/button_reward_check.png',
    'use': './pic/button_use.png',
    'mainui_sign': './pic/mainui_sign.png'
}

k_button_img = {}


def has_button(hWnd, button_img, thr):
    img = win32_helper.screenshot(hWnd)
    i, j, val = dip.template_match(img, button_img)
    return val >= thr, i, j, val


def press_button(hWnd, button_img, thr):
    old_hWnd = win32gui.GetForegroundWindow()

    ret, i, j, val = has_button(hWnd, button_img, thr)
    if not ret:
        return False, val

    win32_helper.send_lbutton_clk_to_window(
        hWnd, i + button_img.shape[1] / 2, j + button_img.shape[0] / 2)

    try:
        win32gui.SetForegroundWindow(old_hWnd)
    except:
        pass

    return True, val


def has_button_aux(hWnd, name, thr=0.75):
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    template = k_button_img[name]
    return has_button(hWnd, template, thr)[0]


def press_button_aux(hWnd, name, stride, thr=0.75, op_delay=2):
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    template = k_button_img[name]
    while 1:
        ret, val = press_button(hWnd, template, thr)
        win32_helper.wait(op_delay)
        if not stride or not has_button(hWnd, template, thr)[0]:
            break
    if ret:
        print('press button {0}, val = {1}'.format(name, val))
    else:
        print('no find button {0}, val = {1}'.format(name, val))
    return ret


# 点击略过
def press_button_skip(hWnd, stride=True):
    return press_button_aux(hWnd, 'skip', stride)


def has_button_skip(hWnd):
    return has_button_aux(hWnd, 'skip')


# 点击确定
def press_button_ok(hWnd, stride=True):
    return press_button_aux(hWnd, 'ok', stride)


def has_button_ok(hWnd):
    return has_button_aux(hWnd, 'ok')


# 点击取消
def press_button_cancel(hWnd, stride=True):
    return press_button_aux(hWnd, 'cancel', stride)


def has_button_cancel(hWnd):
    return has_button_aux(hWnd, 'cancel')


# 点击挑战
def press_button_battle_start(hWnd, stride=True):
    return press_button_aux(hWnd, 'battle_start', stride)


def has_button_battle_start(hWnd):
    return has_button_aux(hWnd, 'battle_start')


# 点击确认
def press_button_reward_check(hWnd, stride=True):
    return press_button_aux(hWnd, 'reward_check', stride)


def has_button_reward_check(hWnd):
    return has_button_aux(hWnd, 'reward_check')


# 点击使用
def press_button_use(hWnd, stride=False):
    return press_button_aux(hWnd, 'use', stride)


def has_button_use(hWnd):
    return has_button_aux(hWnd, 'use')


# 判断是否在主界面
def has_mainui_sign(hWnd):
    return has_button_aux(hWnd, 'mainui_sign')


if __name__ == "__main__":
    handle = win32_helper.find_window_handle('MuMu', None, None)
    handle = win32_helper.find_first_child_window(handle)
    ret = has_button_aux(handle, 'cancel')
    print(ret)
