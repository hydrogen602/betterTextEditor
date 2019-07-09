
from shutil import get_terminal_size


# t.columns
# t.lines

class renderer:

    def __init__(self):
        self.size = get_terminal_size((0, 0))
        #print('\033[2J\033[0;0H', end='')
        self.clear()
    
    def clear(self):
        for _ in range(self.size.columns):
            print('\033[A\r\033[K', end='')

    def print(self, text, end=''):
        print(text, end=end)

    def println(self, text):
        print(text, end='\n')