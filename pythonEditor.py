
import menu
import time

from keyword import kwlist

'''
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
'''

class editor:

    def __init__(self, m):
        self.m = m
        self.m.window.scrollok(True)
        self.lines = ['' for i in range(self.m.height - 2)]

    def print(self, text, row, color=16):
        prevText = self.lines[row]
        col = len(prevText)
        self.m.window.addstr(row, col, text, menu.curses.color_pair(color))
        self.lines[row] = prevText + text

    def load(self, pathAndFile):
        text = None
        try:
            f = open(pathAndFile)
            text = f.read()
        except FileNotFoundError as e:
            text = 'File Not Found'
        finally:
            f.close()

        text = text.split('\n')
        global log
        #log.write(f'{self.m.height}')
        for i in range(self.m.height - 2):
            log.write(text[i] + '\n')
            self.print(text[i], i)

log = None

def main():
    global log
    with menu.main() as m:
        log = open('info.log', 'w')
        #log.write('test')

        e = editor(m)
        e.load('main.py')
        
        row = 2
        for i in range(0, 255):
           col = i % m.width
           row = i // m.width + 2
           m.window.addstr(row, col, 'X', menu.curses.color_pair(i))

        #e.print('def', 0, 209) #209
        #e.print(' ', 0)
        #e.print('func', 0, 47)
        #e.print('():', 0)
        #e.print('    a', 1)

        # 173, 15

        m.run()

try:
    main()
except Exception as e:
    if e.args[0] != 'exiting':
        raise
finally:
    if log:
        log.close()