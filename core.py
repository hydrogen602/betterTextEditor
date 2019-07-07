
import curses

class main():

    def __init__(self):
        self.window = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()

        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, i, -1)

        self.height, self.width = self.window.getmaxyx()

        self.__y = 0
        self.__x = 0

        self.__buf = bytearray()

        self.isRunning = False

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        curses.endwin()

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
            if k == 10:
                self.__buf = bytearray()
                k = 'down'

            elif k == 127:
                if len(self.__buf) > 0:
                    self.__buf = self.__buf[:-1]
                    if self.__x > 0:
                        # delete prev char
                        self.window.addstr(self.__y, self.__x - 1, ' ')
                        self.__x -= 1


            elif k < 256:
                self.__buf.append(k)
                
                self.window.addstr(self.__y, self.__x, bytearray([k]).decode())

                self.__x += 1 # crashable

        if k == 'up' and self.__y > 0:
            self.__y -= 1
        elif k == 'down':
            self.__y += 1
        elif k == 'right':
            self.__x += 1
        elif k == 'left':
            self.__x -= 1

    def run(self):
        self.isRunning = True
        try:
            while True:
                self.processKey()
                self.window.move(self.__y, self.__x)
        finally:
            curses.endwin()

if __name__ == '__main__':
    with main() as m:
        m.run()
