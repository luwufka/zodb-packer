from colorama import Fore, Style, Back
from datetime import datetime

def get_time() -> str:
    return datetime.now().strftime("%d.%m.%y %H:%M:%S")[:-3]
    
RESET = Style.RESET_ALL
TIME_TITLE = Back.LIGHTMAGENTA_EX + Fore.BLACK
LOGGER_TITLE = Back.WHITE + Fore.BLACK
MSG_TITLE = Fore.WHITE + Style.BRIGHT

class Logger:
    def __init__(self, name: str = "LOGGER"):
        self.Name = name
    def info(self, message: str):
        print(f"{LOGGER_TITLE} {self.Name} {RESET} >> {TIME_TITLE} {get_time()} {RESET} {Fore.BLUE}[ INFO ]{RESET} {MSG_TITLE}{message}{RESET}")

    def success(self, message: str):
        print(f"{LOGGER_TITLE} {self.Name} {RESET} >> {TIME_TITLE} {get_time()} {RESET} {Fore.LIGHTGREEN_EX}[ SUCCESS ]{RESET} {MSG_TITLE}{message}{RESET}")

    def warning(self, message: str):
        print(f"{LOGGER_TITLE} {self.Name} {RESET} >> {TIME_TITLE} {get_time()} {RESET} {Fore.YELLOW}[ WARNING ]{RESET} {MSG_TITLE}{message}{RESET}")

    def error(self, message: str):
        print(f"{LOGGER_TITLE} {self.Name} {RESET} >> {TIME_TITLE} {get_time()} {RESET} {Fore.LIGHTRED_EX}[ ERROR ]{RESET} {MSG_TITLE}{message}{RESET}")