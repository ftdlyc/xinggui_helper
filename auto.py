# 自动刷本
# 使用方法 python ./auto.py 10 1000
# 输入参数两个，第一个为战斗时间(秒)，第二个为循环次数

import sys
import game
import win32_helper

if len(sys.argv) != 3:
    print('format: python ./auto.py 战斗时间 循环次数')
    exit()

hWnd = win32_helper.find_window_handle('MuMu', None, None)
hWnd = win32_helper.find_first_child_window(hWnd)

for i in range(int(sys.argv[2])):
    print('\nloop {0}'.format(i))
    i += 1

    win32_helper.wait(3)
    win32_helper.send_key_to_window(hWnd, win32_helper.VK_X)

    game.battle(hWnd, battle_cost_times=int(sys.argv[1]))
