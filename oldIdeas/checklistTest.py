
import curses
from shutil import get_terminal_size
import time

# get_terminal_size((0, 0))

#

class main():

    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()
        curses.start_color()
        curses.use_default_colors()

        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)

        self.height, self.width = self.window.getmaxyx()
        self.x, self.y = 0, 0

    def captureKey(self):
        a = [self.window.getch()]

        self.window.nodelay(True)
        
        while True:
            i = self.window.getch()
            if i == -1: break
            a.append(i)

        self.window.nodelay(False)

        if len(a) == 1:
            return a[0]

        if a == [27, 91, 66]:
            return 'down'
        if a == [27, 91, 67]:
            return 'right'
        if a == [27, 91, 68]:
            return 'left'
        if a == [27, 91, 65]:
            return 'up'

        return a

    def setPosition(self):
        self.window.move(self.y, self.x)

    def processKey(self):
        k = self.captureKey()
        if type(k) == int:
            return k

        if k == 'up':
            if self.y > 0:
                self.y -= 1
        elif k == 'down':
            if self.y < self.height - 1:
                self.y += 1
        if k == 'left':
            if self.x > 0:
                self.x -= 1
        elif k == 'right':
            if self.x < self.width - 1:
                self.x += 1

        self.setPosition()        

    def run(self):
        self.window.move(self.y, self.x)

        while True:
            a = self.processKey()
            if a == 10:
                break
       
        self.window.addstr(str([self.height, self.width]))

        for c in range(255):
            self.window.addstr(3 + c // self.width, c % self.width, 'X', curses.color_pair(c))

        t = self.window.getstr()



try:
    m = main()
    m.run()
finally:
    curses.endwin()
