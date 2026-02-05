# Basic colors
print("\033[91mRed text\033[0m")
print("\033[92mGreen text\033[0m")
print("\033[93mYellow text\033[0m")
print("\033[94mBlue text\033[0m")

# With background colors
print("\033[41mRed background\033[0m")
print("\033[42mGreen background\033[0m")

# Bold, underline, etc.
print("\033[1mBold text\033[0m")
print("\033[4mUnderlined text\033[0m")


# Red and bold
print("\033[1;91mRed and bold text\033[0m")

# Or using separate codes (same result)
print("\033[1m\033[91mRed and bold text\033[0m")


# Green and bold
print("\033[1;92mGreen and bold\033[0m")

# Yellow and bold
print("\033[1;93mYellow and bold\033[0m")

# Blue and bold
print("\033[1;94mBlue and bold\033[0m")

# Red, bold, and underlined
print("\033[1;4;91mRed, bold, and underlined\033[0m")

# Bold with red background
print("\033[1;41mBold with red background\033[0m")

# Green text on blue background, bold
print("\033[1;92;44mGreen on blue, bold\033[0m")
```

## ANSI code reference:
```
Style codes:
  0  - Reset
  1  - Bold
  2  - Dim
  4  - Underlined
  5  - Blink

Foreground (text) colors:
  91 - Bright Red
  92 - Bright Green
  93 - Bright Yellow
  94 - Bright Blue
  95 - Bright Magenta
  96 - Bright Cyan

Background colors:
  41 - Red background
  42 - Green background
  43 - Yellow background
  44 - Blue background


from colorama import Fore, Back, Style, init

init(autoreset=True)  # Auto-reset colors after each print

print(Fore.RED + "Red text")
print(Fore.GREEN + "Green text")
print(Fore.YELLOW + "Yellow text")
print(Back.BLUE + "Blue background")
print(Style.BRIGHT + "Bright text")

# pip install termcolor
from termcolor import colored

print(colored("Hello world", "red"))
print(colored("Bold green", "green", attrs=["bold"]))
print(colored("Yellow on blue", "yellow", "on_blue"))


from rich import print

print("[bold red]Bold red text[/bold red]")
print("[green]Green text[/green]")
print("[yellow on blue]Yellow on blue[/yellow on blue]")
