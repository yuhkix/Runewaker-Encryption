import shutil
import pyperclip
import os
from utility.logs import CustomLogger
from utility.const import (LIGHT_RED, RESET)

logger = CustomLogger()

def get_console_width():
    """Get the current console width."""
    size = shutil.get_terminal_size((80, 20))
    return size.columns

def center_text(text):
    """Center text in the console."""
    console_width = get_console_width()
    for line in text.splitlines():
        print(line.center(console_width))
        
def output(text: str, file_name: str) -> None:
    """Writes the provided text to the specified file, clearing the file first.

    Args:
        text (str): The text to write to the file.
        file_name (str): The name of the file (including path if necessary).
    """
    with open(file_name, 'w') as file:
        file.write(text)
        
def clipboard(text: str) -> None:
    """Copies the provided text to the clipboard.

    Args:
        text (str): The text to copy to the clipboard.
    """
    pyperclip.copy(text)
    logger.log("Copied to clipboard.", "info", color="80a2de")
    
def watermark():
    """Display watermark in console."""
    ascii_art = r"""
 ██▀███   █    ██  ███▄    █ ▓█████  █     █░ ▄▄▄       ██ ▄█▀▓█████  ██▀███  
▓██ ▒ ██▒ ██  ▓██▒ ██ ▀█   █ ▓█   ▀ ▓█░ █ ░█░▒████▄     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▓██  ▒██░▓██  ▀█ ██▒▒███   ▒█░ █ ░█ ▒██  ▀█▄  ▓███▄░ ▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ▓▓█  ░██░▓██▒  ▐▌██▒▒▓█  ▄ ░█░ █ ░█ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒▒▒█████▓ ▒██░   ▓██░░▒████▒░░██▒██▓  ▓█   ▓██▒▒██▒ █▄░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▓░▒ ▒   ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░  ▒ ░ ░    ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░░   ░  ░░░ ░ ░    ░   ░ ░    ░     ░   ░    ░   ▒   ░ ░░ ░    ░     ░░   ░ 
   ░        ░              ░    ░  ░    ░          ░  ░░  ░      ░  ░   ░     
                                                                               """
    center_text(f"{LIGHT_RED}{ascii_art}{RESET}")

def clear_console():
    """Clear console based on the operating system."""
    os.system("title Runewaker Encryption")
    os.system('cls' if os.name == 'nt' else 'clear')