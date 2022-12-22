from colorama import  init,Fore,Back,Style
init(autoreset=True)
class Colored(object):

    #  fore color:red  back color:default
    def red(self, s):
        return Fore.RED + s + Fore.RESET

    #  fore color:green  back color:default 加粗
    def green(self, s):
        return Style.BRIGHT + Fore.GREEN + s + Fore.RESET

    #  fore color:yellow  back color:default
    def yellow(self, s):
        return Fore.YELLOW + s + Fore.RESET

    #  fore color:蓝色  back color:default
    def blue(self, s):
        return Style.BRIGHT + Fore.BLUE + s + Fore.RESET

    #  fore color:洋红色  back color:default
    def magenta(self, s):
        return Fore.MAGENTA + s + Fore.RESET

    #  fore color:青色  back color:default
    def cyan(self, s):
        return Fore.CYAN + s + Fore.RESET

    #  fore color:白色  back color:default
    def white(self, s):
        return Fore.WHITE + s + Fore.RESET

    #  fore color:黑色  back color:default
    def black(self, s):
        return Fore.BLACK

    #  fore color:白色  back color:绿色
    def white_green(self, s):
        return Fore.WHITE + Back.GREEN + s

    def dave(self, s):
        return Style.BRIGHT + Fore.GREEN + s
    
class Printer(object):
    def __init__(self):
        self.color = Colored()
    
    def hint(self, content):
        print(self.color.green(content))

    def info(self, content):
        print("    ", content)
        
    def err(self, content):
        print(self.color.red(content))

    def session(self, func, params):
        print(self.color.blue('Session: ' + func))