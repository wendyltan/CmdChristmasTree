# greeting.py

from colorama import Fore
import random

def colorful_greeting(text):
    color_codes = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]
    random_color = random.choice(color_codes)
    return f"{random_color}{text}{Fore.RESET}"
