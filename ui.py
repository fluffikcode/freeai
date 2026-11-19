"""Цвета, лого, утилиты вывода."""

RESET = "\033[0m"
WHITE = "\033[97m"
GRAY  = "\033[90m"
BOLD  = "\033[1m"

# 3D-лого freeai (белый = основной, серый = тень/обводка)
LOGO = [
    f"{GRAY}   ▄▄▄▄▄▄  ▄▄▄▄▄▄  ▄▄▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄  ▄▄▄{RESET}",
    f"{WHITE}   ██▀▀▀▀  ██▀▀██  ██▀▀▀▀  ██▀▀▀▀  ██▀██ ██▀██{RESET}",
    f"{WHITE}   ████▄▄  ██████  ████▄▄  ████▄▄  █████ █████{RESET}",
    f"{WHITE}   ██      ██  ██  ██      ██      ██  █ ██  █{RESET}",
    f"{GRAY}   ▀▀      ▀▀  ▀▀  ▀▀▀▀▀▀  ▀▀▀▀▀▀  ▀▀  ▀ ▀▀  ▀{RESET}",
    "",
    f"{GRAY}   ───────────────────────────────────────────{RESET}",
    f"{WHITE}   f r e e a i{RESET}   {GRAY}· terminal client{RESET}",
    f"{GRAY}   ───────────────────────────────────────────{RESET}",
]

def print_logo():
    print()
    for line in LOGO:
        print(line)
    print()

def white(text):
    return f"{WHITE}{text}{RESET}"

def gray(text):
    return f"{GRAY}{text}{RESET}"

def divider():
    print(gray("   " + "─" * 43))

def success(msg):
    print(gray(f"   ✓ {msg}"))

def error(msg):
    print(gray(f"   ✗ {msg}"))
