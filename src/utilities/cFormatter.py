# Authors
# Organization: https://github.com/rogueEdit/
# Repository: https://github.com/rogueEdit/OnlineRogueEditor
# Contributors: https://github.com/claudiunderthehood https://github.com/JulianStiebler/
# Date of release: 04.06.2024 

from colorama import Fore, Style, init
from enum import Enum
import logging
import shutil

class Color(Enum):
    CRITICAL = Style.BRIGHT + Fore.RED
    DEBUG = Style.BRIGHT + Fore.BLUE
    ERROR = Fore.RED
    WARNING = Fore.YELLOW
    INFO = Style.BRIGHT + Fore.LIGHTYELLOW_EX
    
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    BRIGHT_BLACK = Style.BRIGHT + Fore.BLACK
    BRIGHT_RED = Style.BRIGHT + Fore.RED
    BRIGHT_GREEN = Style.BRIGHT + Fore.GREEN
    BRIGHT_YELLOW = Style.BRIGHT + Fore.YELLOW
    BRIGHT_BLUE = Style.BRIGHT + Fore.BLUE
    BRIGHT_MAGENTA = Style.BRIGHT + Fore.MAGENTA
    BRIGHT_CYAN = Style.BRIGHT + Fore.CYAN
    BRIGHT_WHITE = Style.BRIGHT + Fore.WHITE

class cFormatter(logging.Formatter):
    """
    A custom formatter for logging.
    """
    LOG_LEVELS = {
        logging.CRITICAL: Color.CRITICAL,
        logging.DEBUG: Color.DEBUG,
        logging.ERROR: Color.ERROR,
        logging.WARNING: Color.WARNING,
        logging.INFO: Color.INFO,
    }

    @staticmethod
    def print(color: Color, text: str, isLogging: bool = False) -> None:
        """
        Logs the text to the file without color and prints it to the console with color.
        Args:
            color (Color): The color index to use for formatting.
            text (str): The text to log.
            isLogging (bool, optional): Specifies whether the text is for logging. Defaults to False.
        """
        logger = logging.getLogger('root')
        if isLogging:
            # Determine the logging level based on color
            log_level = logging.INFO
            for level, col in cFormatter.LOG_LEVELS.items():
                if col == color:
                    log_level = level
                    break
            logger.log(log_level, text)

        color_code = color.value
        formatted_text = f'{color_code}{text}{Style.RESET_ALL}'
        print(formatted_text)  # Print to console with color

    @staticmethod
    def print_separators(num_separators: int = None, separator: str = '-', color: Color = None) -> None:
        """
        Prints separators with the specified color.
        Args:
            num_separators (int, optional): The number of separators to print. If None, uses the terminal width. Defaults to None.
            separator (str, optional): The character used for the separators. Defaults to '-'.
            color (Color, optional): The color to use for the separators. Defaults to None.
        """
        if num_separators is None:
            terminal_width = shutil.get_terminal_size().columns
            num_separators = terminal_width

        color_code = color.value if color else ''
        formatted_separators = f'{color_code}{separator * num_separators}{Style.RESET_ALL}'
        print(formatted_separators)