# 自动塔
# 使用方法 python ./tower.py 30
# 输入参为战斗时间(秒)

import sys
import game
import win32_helper

if len(sys.argv) != 2:
    print('format: python ./tower.py 战斗时间')
    exit()

hWnd = win32_helper.find_window_handle('MuMu', None, None)
hWnd = win32_helper.find_first_child_window(hWnd)

op_delay = 3

i = 0
while True:
    print('\nloop {0}'.format(i))
    i += 1

    win32_helper.send_key_to_window(hWnd, win32_helper.VK_Y)

    win32_helper.wait(op_delay)
    if game.has_select_box(hWnd):
        game.press_button_cancel(hWnd)
        continue
        
    game.battle(hWnd, battle_cost_times=int(sys.argv[1]))
    win32_helper.wait(14.5 * 60)
