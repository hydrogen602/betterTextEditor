
import curses


import curses
from shutil import get_terminal_size
import time

# get_terminal_size((0, 0))

#

class main():

    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()

        self.height, self.width = self.window.getmaxyx()

        self.boxes = [(0, 0)]
        self.indexOfBoxes = 0

    def addBox(self, y, x):
        self.boxes.append((y, x))

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
        self.window.move(*self.boxes[self.indexOfBoxes])

    def processKey(self):
        k = self.captureKey()
        if type(k) == int:
            return k

        if k == 'up' or k == 'left':
            self.indexOfBoxes += 1
            self.setPosition()
        elif k == 'down' or k == 'right':
            pass

        self.setPosition()        

    def run(self):
        self.window.move(0, 0)

        self.addBox(10, 0)

        while True:
            a = self.processKey()
            if a == 10:
                break
       
        self.window.addstr(str([self.height, self.width]))

        t = self.window.getstr()




try:
    m = main()
    m.run()
finally:
    curses.endwin()
