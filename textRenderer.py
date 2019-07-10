
import core
import time

# Idea: make it auto detect key methods using dir() and then run
# them using getattr()


class TextRenderer(core.Main):


    def __init__(self):
        super(TextRenderer, self).__init__()
        self.log.write('hi\n')

        self.lines = ['']

        self.scrollY = 0
        self.scrollX = 0

        self.lastX = 0

        self.lastKeyPress = { 'type': None, 'time': 0 }

        self.pathAndFile = None


    def load(self, pathAndFile):
        self.pathAndFile = pathAndFile

        text = None
        try:
            f = open(pathAndFile)
            text = f.read()
        except FileNotFoundError as e:
            text = 'File Not Found'
        finally:
            f.close()

        text = text.split('\n')

        self.log.write(f'loaded: {pathAndFile}\n')
        self.log.write(f'length: {len(text)}\n')

        self.lines = []
        for line in text:
            self.lines.append(line)

        self.updateScreen()


    def print(self, text, row, color=16, resetX=False):
        if row == len(self.lines):
            # new line
            self.lines.append('')
        
        if resetX: # start at the beginning of the line
            prevText = ''
            col = 0
        else:
            prevText = self.lines[row]
            col = len(prevText)

        if col + len(text) >= self.width:
            visibleText = text[:self.width - col - 1]
        else:
            visibleText = text

        self.window.addstr(row, col, visibleText, core.curses.color_pair(color))

        if not resetX:
            self.lines[row] = prevText + text


    def processKey(self, k):
        options = {
            'down': self.keyDown,
            'up': self.keyUp,
            'left': self.keyLeft,
            'right': self.keyRight
        }

        update = False

        if k in options:
            function = options[k]
            update = function()

        self.lastKeyPress['type'] = k
        self.lastKeyPress['time'] = time.time()

        if update:
            self.updateScreen()


    def isAccelerated(self, k):
        timeDif = abs(time.time() - self.lastKeyPress['time'])

        return self.lastKeyPress['type'] == k and timeDif < 0.12


    def keyDown(self):
        if self.isAccelerated('down'):
            step = 3
        else:
            step = 1

        if not self.y + self.scrollY < len(self.lines) - step:
            return

        # self.log.write(f'time: {time.time():.2f}\n')
        # self.log.write(f'step: {step}\n')
        # self.log.write(f'scrollY: {self.scrollY}\n\n')

        update = False

        if self.y < self.height - step:
            self.y += step
        else:
            self.scrollY += step - (self.height - self.y - 1)
            self.y = self.height - 1
            update = True

        if self.bounds():
            update = True

        return update


    def keyUp(self):
        if self.isAccelerated('up'):
            step = 3
        else:
            step = 1

        # self.log.write(f'time: {time.time():.2f}\n')
        # self.log.write(f'step: {step}\n')
        # self.log.write(f'scrollY: {self.scrollY}\n\n')

        if not self.y + self.scrollY > step - 1:
            return

        update = False

        if self.y > step - 1:
            self.y -= step
        else: # the condition where scrollY = 0 and y = 0 is convered by the outer if statement
            self.scrollY -= step - self.y
            self.y = 0
            update = True

        if self.bounds():
            update = True    

        return update


    def keyLeft(self):
        update = False

        if self.x + self.scrollX > 0:
            if self.x > 0:
                self.x -= 1
            else:
                self.scrollX -= 1
                update = True

        elif self.y + self.scrollY > 0:
            # last character
            if self.keyUp():
                update = True

            length = len(self.lines[self.y + self.scrollY])

            self.x = length - self.scrollX
            if self.x > self.width:
                self.x = self.width - 1
                self.scrollX = length - self.x
                update = True

        self.lastX = self.x + self.scrollX

        return update


    def keyRight(self):
        length = len(self.lines[self.y + self.scrollY])

        update = False
        
        if self.x + self.scrollX < length:
            if self.x < self.width - 1:
                self.x += 1
            else:
                self.scrollX += 1
                update = True
        else:
            # next line

            value = self.keyDown()
            if value:
                update = True

            if value == None:
                return

            self.x = 0
            self.scrollX = 0

        self.lastX = self.x + self.scrollX

        return update


    def bounds(self):
        self.x = self.lastX - self.scrollX

        update = False

        length = len(self.lines[self.y + self.scrollY])

        if self.x < 0:
            self.scrollX -= abs(self.x)
            self.x = 0
            update = True

        elif self.x >= self.width:
            self.scrollX += self.x - self.width 
            self.x = self.width - 1
            update = True

        if self.x + self.scrollX > length:
            #self.x + self.scrollX = length
            if self.scrollX > length:
                self.scrollX = length
                self.x = 0
                update = True
            else:
                self.x = length - self.scrollX

        return update


    def updateScreen(self):
        self.window.erase()
        self.window.refresh()

        #self.log.write(f'updating! {self.scrollY}\n')

        for i in range(self.height):
            if self.scrollY + i >= len(self.lines):
                break

            entireLine = self.lines[self.scrollY + i]
            visibleLine = entireLine[self.scrollX:self.scrollX + self.width]

            self.print(visibleLine, i, resetX=True)



if __name__ == '__main__':
    with TextRenderer() as m:
        m.load('main.py')
        m.run()


