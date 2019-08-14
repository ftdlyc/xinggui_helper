# 自动铁5

import win32_helper

handle = win32_helper.find_window_handle("MuMu", None, None)
handle = win32_helper.find_first_child_window(handle)

i = 0
while True:
    win32_helper.wait(6)
    win32_helper.send_key_to_window(handle, win32_helper.VK_X)
    win32_helper.wait(3)
    win32_helper.send_key_to_window(handle, win32_helper.VK_X)
    win32_helper.wait(3)
    win32_helper.send_key_to_window(handle, win32_helper.VK_C)
    win32_helper.wait(4)
    win32_helper.send_key_to_window(handle, win32_helper.VK_X)
    win32_helper.wait(3)
    win32_helper.send_key_to_window(handle, win32_helper.VK_C)
    win32_helper.wait(180)
    win32_helper.send_key_to_window(handle, win32_helper.VK_X)
    win32_helper.wait(2)
    win32_helper.send_key_to_window(handle, win32_helper.VK_X)

    print("loop {0}".format(i))
    i += 1
