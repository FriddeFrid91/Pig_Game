"""Colors class. Use colors in your script."""


class colors:
    class TextStyles:
        RESET = '\033[0m'      # Reset to default colors and styles
        BOLD = '\033[1m'       # Bold text
        ITALIC = '\033[3m'     # Italic text (not widely supported)
        UNDERLINE = '\033[4m'  # Underline text
        BLINK = '\033[5m'      # Blinking text (not widely supported)
        REVERSE = '\033[7m'    # Reverse colors (swap foreground and background)
        HIDDEN = '\033[8m'
      

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PINK = '\033[95m'
    CYAN = '\033[96m'
    RESET = '\033[0m'  # Reset to default colors.

