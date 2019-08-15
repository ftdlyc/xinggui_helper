# 2019.8.14
# by ftdlyc

import win32gui
import win32_helper
import dip


# 按钮
def press_button(hWnd, button_img, thr):
    old_hWnd = win32gui.GetForegroundWindow()

    img = win32_helper.screenshot(hWnd)
    i, j, val = dip.template_match(img, button_img)
    if val < thr:
        return False, val
    win32_helper.send_lbutton_clk_to_window(
        hWnd, i + button_img.shape[1] / 2, j + button_img.shape[0] / 2)

    try:
        win32gui.SetForegroundWindow(old_hWnd)
    except:
        pass

    return True, val
