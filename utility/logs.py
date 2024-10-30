from utility.const import RESET

class CustomLogger:
    def _format_message(self, message, log_type=None, color_code=None):
        """Formats the log message with optional log type and color."""
        if log_type and color_code:
            colored_log_type = f"{color_code}{log_type.upper()}{RESET}"
            return f"{colored_log_type} - {message}"
        else:
            return f"{message}"

    def _convert_color(self, color):
        """Converts color from hex, RGB, or leaves ANSI codes as-is."""
        if isinstance(color, str) and color.startswith("\033["):
            return color
        if isinstance(color, str):
            color = color.lstrip("#")
            r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
        elif isinstance(color, tuple) and len(color) == 3:
            r, g, b = color
        else:
            raise ValueError("Color must be a hex string, an RGB tuple, or an ANSI code")

        return f"\033[38;2;{r};{g};{b}m"

    # log_type (e.g., "warning", "info", "success" or "error")
    # color (e.g., color="#1ed760" or color="1ed760" for hex and color=(232, 87, 91) for rgb)
    def log(self, message, log_type=None, color=None):
        """Logs a message with optional type and color, creating a new file if the day changes."""
        color_code = self._convert_color(color) if color else ""
        log_message = self._format_message(message, log_type, color_code)
        print(log_message)