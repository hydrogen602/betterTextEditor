
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

        self.boxes = []
        self.indexOfBoxes = None
        self.labels = []
        self.isRunning = False

    def addBox(self, y, x, func=lambda x: None, lim=-1, buf='', index=None):
        box = {'y': y, 'x': x, 'func': func, 'buf': bytearray(buf.encode()), 'lim': lim}
        if index:
            self.boxes.insert(index, box)
        else:
            self.boxes.append(box)
        self.window.addstr(y, x, buf)
        return box

    def addLabel(self, y, x, text):
        self.labels.append({'y': y, 'x': x, 'text': text})
        self.window.addstr(y, x, text)

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
            box = self.boxes[self.indexOfBoxes]
            self.window.move(box['y'], box['x'])
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
            box = self.boxes[self.indexOfBoxes]

            if k == 10:
                self.window.addstr(box['y'], box['x'], ' ' * len(box['buf']))

                self.boxes[self.indexOfBoxes]['func'](box['buf'])
                
                box['buf'] = bytearray()


            elif k == 127:
                if len(box['buf']) > 0:
                    box['buf'] = box['buf'][:-1]
                    self.window.addstr(box['y'], box['x'] + len(box['buf']), ' ')
            elif k < 256:
                if box['lim'] < 0 or len(box['buf']) < box['lim']:
                    box['buf'].append(k)
                
                    self.window.addstr(box['y'], box['x'], box['buf'].decode())
            
            #self.window.addstr(1, 0, str(k))
            
                

        if (k == 'up' or k == 'left') and self.indexOfBoxes > 0:
            self.indexOfBoxes -= 1
        elif (k == 'down' or k == 'right') and self.indexOfBoxes < len(self.boxes) - 1:
            self.indexOfBoxes += 1

    def run(self):
        self.isRunning = True
        try:
            self.makeCmdLine()
            self.indexOfBoxes = len(self.boxes) - 1

            while True:
                self.processKey()
                box = self.boxes[self.indexOfBoxes]
                #if box['lim'] == 1:
                #    self.window.move(box['y'], box['x'])
                #else:
                self.window.move(box['y'], box['x'] + len(box['buf']))
        finally:
            curses.endwin()

if __name__ == '__main__':
    m = main()
    m.run()
