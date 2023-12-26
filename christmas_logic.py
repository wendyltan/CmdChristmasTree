
import time
import threading
from Christmas import draw_christmas_tree
from greeting import colorful_greeting
from colorama import Fore, Style

def print_colored_tree(tree_height, greeting_text, stop_flag):
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    trunk_thickness = tree_height // 3
    trunk_padding = (2 * tree_height - 1 - trunk_thickness) // 2

    try:
        while not stop_flag.is_set():
            for color in colors:
                tree_lines = draw_christmas_tree(tree_height)
                for i, line in enumerate(tree_lines):
                    if i == len(tree_lines) - 1:
                        print(color + line + Style.RESET_ALL)
                    else:
                        print(color + line)

                # 获取树的底部行的下一行位置
                bottom_line_position = len(tree_lines)

                # 输出祝福语，确保在树干下方居中显示
                trunk_padding = (2 * tree_height - 1 - tree_height // 3) // 2
                print(' ' * trunk_padding + '\033[{};0H'.format(bottom_line_position) + colorful_greeting(greeting_text))

                time.sleep(1)  # 刷新频率调整为1秒

                # 清空控制台
                print('\033[H\033[J', end='', flush=True)

    except KeyboardInterrupt:
        pass