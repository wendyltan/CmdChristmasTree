import random
from colorama import Fore, Style, init

# 初始化 colorama
init()

def draw_christmas_tree(height):
    tree_lines = []
    for i in range(height):
        spaces = ' ' * (height - i - 1)
        stars = '*' * (2 * i + 1)
        colored_stars = ''.join(random.choice([
            Fore.RED + '*' + Style.RESET_ALL,
            Fore.GREEN + '*' + Style.RESET_ALL,
            Fore.YELLOW + '*' + Style.RESET_ALL,
            Fore.CYAN + '*' + Style.RESET_ALL,
            Fore.MAGENTA + '*' + Style.RESET_ALL
        ]) for _ in stars)

        tree_lines.append(spaces + colored_stars)

    trunk_thickness = height // 3  # 树干厚度随树高而增加
    trunk_padding = (2 * height - 1 - trunk_thickness) // 2
    colored_trunk = Fore.YELLOW + ' ' * trunk_padding + '|' * trunk_thickness + ' ' * trunk_padding + Style.RESET_ALL
    tree_lines.append(colored_trunk)  # 将树干插入到树的最后一行底部

    return tree_lines