import os

# windows bug
os.system("")


class Cologger:
    def __init__(self):
        self.color = None
        self.bg_color = None
        self.fmt = None

    def set_fmt(self, fmt):
        if fmt == "bold":
            self.fmt = Formaters.BOLD
        elif fmt == "italic":
            self.fmt = Formaters.ITALIC
        elif fmt == "underline":
            self.fmt = Formaters.UNDERLINE
        elif fmt == "selected":
            self.fmt = Formaters.SELECTED
        elif fmt == "strikethrough":
            self.fmt = Formaters.STRIKETHORUGH
        else:
            raise Exception("Please pass a valid format.")

    def set_color(self, color, custom=""):
        if color == "black":
            self.color = Colors.BLACK
        elif color == "red":
            self.color = Colors.RED
        elif color == "green":
            self.color = Colors.GREEN
        elif color == "yellow":
            self.color = Colors.YELLOW
        elif color == "green":
            self.color = Colors.GREEN
        elif color == "blue":
            self.color = Colors.BLUE
        elif color == "violet":
            self.color = Colors.VIOLET
        elif color == "cyan":
            self.color = Colors.CYAN
        elif color == "white":
            self.color = Colors.WHITE
        elif color == "custom":
            self.color = "\033[38;2;{};{};{}m{}\033[0m".format(
                str(custom[0]), str(custom[1]), str(custom[2]), "X"
            )
        else:
            raise Exception("Please pass a valid color.")

    def set_bg(self, color, custom=""):
        if color == "black":
            self.bg_color = BackgroundColors.BLACK
        elif color == "red":
            self.bg_color = BackgroundColors.RED
        elif color == "green":
            self.bg_color = BackgroundColors.GREEN
        elif color == "yellow":
            self.bg_color = BackgroundColors.YELLOW
        elif color == "green":
            self.bg_color = BackgroundColors.GREEN
        elif color == "blue":
            self.bg_color = BackgroundColors.BLUE
        elif color == "violet":
            self.bg_color = BackgroundColors.VIOLET
        elif color == "cyan":
            self.bg_color = BackgroundColors.CYAN
        elif color == "white":
            self.bg_color = BackgroundColors.WHITE
        elif color == "custom":
            self.bg_color = "\033[48;2;{};{};{}m{}\033[0m".format(
                str(custom[0]), str(custom[1]), str(custom[2]), "X"
            )
        else:
            raise Exception("Please pass a valid color.")

    def colog(self, *args):
        # If statements:
        # 1. none
        # 2. color
        # 3. bg
        # 4. fmt
        # 5. color, bg
        # 6. color, fmt
        # 7. bg, fmt
        # 8. all

        if self.color != None:
            if "X" in self.color:
                index = self.color.index("X")

                string = ""
                for i in list(args):
                    string += str(i) + " "

                self.color = list(self.color)

                self.color[index] = string
                print("".join(self.color))
                return

        if self.bg_color != None:
            if "X" in self.bg_color:
                index = self.bg_color.index("X")

                string = ""
                for i in list(args):
                    string += str(i) + " "

                self.bg_color = list(self.bg_color)

                self.bg_color[index] = string
                print("".join(self.bg_color))
                return

        if self.color == None and self.bg_color == None and self.fmt == None:
            print(*args)
        elif self.color != None and self.bg_color == None and self.fmt == None:
            print(self.color + cologger_print(*args))
        elif self.color == None and self.bg_color != None and self.fmt == None:
            print(self.bg_color + cologger_print(*args))
        elif self.color == None and self.bg_color == None and self.fmt != None:
            print(self.fmt + cologger_print(*args))
        elif self.color != None and self.bg_color != None and self.fmt == None:
            print(self.color + self.bg_color + cologger_print(*args))
        elif self.color != None and self.bg_color == None and self.fmt != None:
            print(self.color + self.fmt + cologger_print(*args))
        elif self.color != None and self.bg_color == None and self.fmt != None:
            print(self.color + self.fmt + cologger_print(*args))
        elif self.color == None and self.bg_color != None and self.fmt != None:
            print(self.bg_color + self.fmt + cologger_print(*args))
        else:
            print(self.fmt + self.color + self.bg_color + cologger_print(*args))

    def error(self, text):
        return print(Colors.RED + cologger_print(text))

    def info(self, text):
        return print(Colors.WHITE + cologger_print(text))

    def debug_var(self, var):
        return print(f"""\n-----------------------\n{var}\n-----------------------""")

    def reset_color(self):
        self.color = None

    def reset_bg_color(self):
        self.bg_color = None

    def reset_fmt(self):
        self.fmt = None


class Formaters:
    END = "\33[0m"
    BOLD = "\33[1m"
    ITALIC = "\33[3m"
    UNDERLINE = "\33[4m"
    SELECTED = "\33[7m"
    STRIKETHORUGH = '\033[09m'


class Colors:
    BLACK = "\33[30m"
    RED = "\33[31m"
    GREEN = "\33[32m"
    YELLOW = "\33[33m"
    BLUE = "\33[34m"
    VIOLET = "\33[35m"
    CYAN = "\33[36m"
    WHITE = "\33[37m"

    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_VIOLET = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


class BackgroundColors:
    BLACK = "\33[40m"
    RED = "\33[41m"
    GREEN = "\33[42m"
    YELLOW = "\33[43m"
    BLUE = "\33[44m"
    VIOLET = "\33[45m"
    CYAN = "\33[46m"
    WHITE = "\33[47m"

    BRIGHT_BLACK = "\033[100m"
    BRIGHT_RED = "\033[101m"
    BRIGHT_GREEN = "\033[102m"
    BRIGHT_YELLOW = "\033[103m"
    BRIGHT_BLUE = "\033[104m"
    BRIGHT_VIOLET = "\033[105m"
    BRIGHT_CYAN = "\033[106m"
    BRIGHT_WHITE = "\033[107m"


def cologger_print(*args):
    final_str = ""
    for i in list(args):
        final_str += str(i) + " "
    return final_str + Formaters.END


def main():
    cologger = Cologger()
    cologger.set_bg("custom", [255, 255, 255])  # white rgb code
    cologger.colog("Hello Cologger!")


main()
