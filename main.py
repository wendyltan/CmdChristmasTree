# main.py

import socket
socket.setdefaulttimeout(None)

import time
import threading
import keyboard
from colorama import Fore, Style
from christmas_logic import print_colored_tree

# 输入圣诞树的高度和祝福语
tree_height = int(input("请输入圣诞树的高度："))
greeting_text = input("请输入祝福语：")

# 创建线程以在后台运行打印彩色圣诞树的函数
stop_flag = threading.Event()
thread = threading.Thread(target=print_colored_tree, args=(tree_height, greeting_text, stop_flag))
thread.start()

# 等待线程启动
time.sleep(2)

# 检测用户是否按下回车键
input("按下回车键停止刷新，并输出祝福语...")

# 设置停止标志，等待线程结束
stop_flag.set()
thread.join()

# 输出祝福语
trunk_padding = (2 * tree_height - 1 - tree_height // 3) // 2
print(' ' * trunk_padding + colorful_greeting(greeting_text))
