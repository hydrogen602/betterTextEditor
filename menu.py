
import curses


import curses
from shutil import get_terminal_size
import time

# get_terminal_size((0, 0))

# https://docs.python.org/3.7/library/curses.html

class main():

    def __init__(self):
        self.window = curses.initscr()
        curses.noecho()

        self.height, self.width = self.window.getmaxyx()

        self.boxes = [(0, 0, lambda x: None)]
        self.indexOfBoxes = 0
        self.buffer = bytearray()

    def addBox(self, y, x, f=lambda x: None):
        self.boxes.append((y, x, f))

    def makeCmdLine(self):
        def runCmdLine(arg):
            arg = arg.decode().strip()
            if arg == 'quit' or arg == 'exit':
                raise Exception('exiting')

        self.window.addstr(self.height - 2, 0, '-' * self.width)
        self.window.addstr(self.height - 1, 0, '> ')
        self.addBox(self.height - 1, 2, runCmdLine)

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
        try:
            self.window.move(*self.boxes[self.indexOfBoxes][:-1])
        except IndexError as e:
            f = open('error.log', 'w')
            f.write(str(e) + '\n')
            f.write('self.indexOfBoxes = {:d}\n'.format(self.indexOfBoxes))
            f.write('self.boxes = {}\n'.format(self.boxes))
            f.close()
            raise

    def processKey(self):
        k = self.captureKey()
        if type(k) == int:
            y = self.boxes[self.indexOfBoxes][0]
            x = self.boxes[self.indexOfBoxes][1]
            if k == 10:
                self.boxes[self.indexOfBoxes][2](self.buffer)
                self.buffer = bytearray()
            if k == 127:
                if len(self.buffer) > 0:
                    self.buffer = self.buffer[:-1]
                    self.window.addstr(y, x + len(self.buffer), ' ')
            elif k < 256:
                self.buffer.append(k)
                self.window.addstr(3, 0, str(x+len(self.buffer)))
                
                self.window.refresh()

                self.window.addstr(y, x, self.buffer.decode())
            
            self.window.addstr(1, 0, str(k))
            
                

        if (k == 'up' or k == 'left') and self.indexOfBoxes > 0:
            self.indexOfBoxes -= 1
            self.setPosition()
            self.buffer = bytearray()
        elif (k == 'down' or k == 'right') and self.indexOfBoxes < len(self.boxes) - 1:
            self.indexOfBoxes += 1
            self.setPosition()
            self.buffer = bytearray()

        self.setPosition()        

    def run(self):
        self.window.move(0, 0)

        self.makeCmdLine()

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
