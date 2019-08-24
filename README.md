星轨脚本
---
需用管理员权限运行脚本

#### 环境
- python 3.6 or 更高
- pywin32
- numpy
- cv2
- MuMu模拟器

#### 安装
1. 安装python 3.7
2. Powershell/Cmd中输入 pip install pywin32 numpy opencv-python
3. 安装MuMu模拟器, 修改分辨率为1280x720, dpi 300 (若不采用此分辨率需自行更改pic中的模板图)
4. 导入mumu_keys_settings中的按键设置

#### 脚本
- tie5.py 自动铁机队5 (建议把模拟器拖到屏幕右下角, 并且最小化)
- juqing.py 自动刷剧情本 (不能最小化)

#### TODO
- [x] 自动吃AP药(默认4次AP50)
- [x] 刷剧情本
- [ ] 战斗失败返回
