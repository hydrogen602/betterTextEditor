
import curses

class Main():

    def __init__(self):
        self.window = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        #self.window.scrollok(True)
        curses.noecho()

        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)

        self.height, self.width = self.window.getmaxyx()

        self.y = 0
        self.x = 0

        self.__buf = bytearray()

        self.isRunning = False

        self.log = open('core.py.log', 'w')

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        curses.endwin()
        if self.log:
            self.log.close()

    def captureKey(self):
        a = [self.window.getch()]

        self.window.nodelay(True)
        
        while True:
            i = self.window.getch()
            if i == -1: break
            a.append(i)

        self.window.nodelay(False)

        if len(a) == 1:
            k = a[0]
            if k == 127:
                return 'delete'
            elif k == 10:
                return 'return'
            return k

        if a == [27, 91, 66]:
            return 'down'
        if a == [27, 91, 67]:
            return 'right'
        if a == [27, 91, 68]:
            return 'left'
        if a == [27, 91, 65]:
            return 'up'

        return a

    def processKey(self, k):

        if k == 'return':
            self.__buf = bytearray()
            k = 'down'
        elif k == 'delete':
            if len(self.__buf) > 0:
                self.__buf = self.__buf[:-1]
                if self.x > 0:
                    # delete prev char
                    self.window.addstr(self.y, self.x - 1, ' ')
                    self.x -= 1

        if type(k) == int and k < 256:
                self.__buf.append(k)
                
                self.window.addstr(self.y, self.x, bytearray([k]).decode())

                self.x += 1 # crashable

        if k == 'up':
            if self.y > 0:
                self.y -= 1
            else:
                pass # scroll up
        elif k == 'down':
            if self.y < self.height - 1:
                self.y += 1
            else:
                pass # scroll down
        elif k == 'right':
            self.x += 1
        elif k == 'left':
            self.x -= 1

    def run(self):
        self.isRunning = True
        self.window.move(0, 0)
        try:
            while True:
                k = self.captureKey()
                self.processKey(k)
                self.window.move(self.y, self.x)
        finally:
            curses.endwin()

if __name__ == '__main__':
    with Main() as m:
        m.run()
