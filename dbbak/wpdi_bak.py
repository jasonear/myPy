# 2023.11.04
# 备份文件，将服务器bak文件备份到网盘

import os
import shutil

os.system("xcopy I:\\bak\\wpdiweb202306.bak D:\\ZZZ\\000")
# os.system("xcopy I:\\bak\\wpdiweb202306.bak \\\192.168.0.80\\wpdi3\\czg\\sw\\")  #无法复制到网络盘上

shutil.copyfile('I:\\bak\\wpdiweb202306.bak', 'D:\\ZZZ\\000\\test.bak')
# shutil.copyfile('I:\\bak\\wpdiweb202306.bak', '\\\192.168.0.80\\wpdi3\\czg\\sw\\test.bak')  #无法复制到网络盘上
