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
    'cross': './pic/button_cross.png',
    'mainui_sign': './pic/mainui_sign.png'
}

k_button_img = {}
k_thr = 0.75
k_op_delay = 2


def has_button(hWnd, button_img, thr):
    img = win32_helper.screenshot(hWnd)
    ret = dip.template_match(img, button_img)
    return ret[0][0] >= thr, ret[0][1], ret[0][2], ret[0][0]


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


def has_button_aux(hWnd, name, thr=k_thr):
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    template = k_button_img[name]
    return has_button(hWnd, template, thr)[0]


def press_button_aux(hWnd, name, bcheck, thr=k_thr, op_delay=k_op_delay):
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    template = k_button_img[name]
    while 1:
        ret, val = press_button(hWnd, template, thr)
        win32_helper.wait(op_delay)
        if not bcheck or not has_button(hWnd, template, thr)[0]:
            break
    if ret:
        print('press button {0}, val = {1}'.format(name, val))
    else:
        print('no find button {0}, val = {1}'.format(name, val))
    return ret


# 点击略过
def press_button_skip(hWnd, bcheck=True):
    return press_button_aux(hWnd, 'skip', bcheck)


def has_button_skip(hWnd):
    return has_button_aux(hWnd, 'skip')


# 点击确定
def press_button_ok(hWnd, bcheck=True):
    return press_button_aux(hWnd, 'ok', bcheck)


def has_button_ok(hWnd):
    return has_button_aux(hWnd, 'ok')


# 点击取消
def press_button_cancel(hWnd, bcheck=True):
    return press_button_aux(hWnd, 'cancel', bcheck)


def has_button_cancel(hWnd):
    return has_button_aux(hWnd, 'cancel')


# 点击挑战
def press_button_battle_start(hWnd, bcheck=True):
    return press_button_aux(hWnd, 'battle_start', bcheck)


def has_button_battle_start(hWnd):
    return has_button_aux(hWnd, 'battle_start')


# 点击确认
def press_button_reward_check(hWnd, bcheck=True):
    return press_button_aux(hWnd, 'reward_check', bcheck)


def has_button_reward_check(hWnd):
    return has_button_aux(hWnd, 'reward_check')


# 点击使用
def press_button_use(hWnd, bcheck=False):
    return press_button_aux(hWnd, 'use', bcheck)


def has_button_use(hWnd):
    return has_button_aux(hWnd, 'use')


# 点击交叉(x)
def press_button_cross(hWnd, bcheck=False):
    return press_button_aux(hWnd, 'cross', bcheck)


def has_button_cross(hWnd):
    return has_button_aux(hWnd, 'cross')


# 判断是否在主界面
def has_mainui_sign(hWnd):
    return has_button_aux(hWnd, 'mainui_sign')


# 判断是否出现选择框
def has_select_box(hWnd):
    return has_button_ok(hWnd) and has_button_cancel(hWnd)


# 使用AP药
def press_button_use_ap(hWnd, thr=k_thr, op_delay=k_op_delay):
    name = 'use'
    if name not in k_button_img:
        k_button_img[name] = cv2.imread(k_button_path[name])
    button_img = k_button_img[name]

    old_hWnd = win32gui.GetForegroundWindow()

    img = win32_helper.screenshot(hWnd)
    proposal = dip.template_match(img, button_img, n=4)

    button_use = []
    for i in range(4):
        if proposal[i][0] >= k_thr:
            button_use.append(proposal[i])

    def get_third(elem):
        return elem[2]
    button_use.sort(key=get_third, reverse=True)
    
    n = len(button_use)
    if n == 0:
        return False, proposal[0][0]

    i = button_use[0][1]
    j = button_use[0][2]
    win32_helper.send_lbutton_clk_to_window(
        hWnd, i + button_img.shape[1] / 2, j + button_img.shape[0] / 2)

    try:
        win32gui.SetForegroundWindow(old_hWnd)
    except:
        pass

    win32_helper.wait(op_delay)

    return True, button_use[0][0]


if __name__ == "__main__":
    handle = win32_helper.find_window_handle('MuMu', None, None)
    handle = win32_helper.find_first_child_window(handle)
    #ret = has_button_aux(handle, 'cross')
    ret = press_button_use_ap(handle)
    print(ret)
