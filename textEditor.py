
import core
import time

class TextRenderer(core.Main):
    """docstring for TextRenderer"""
    def __init__(self):
        super(TextRenderer, self).__init__()
        self.log.write('hi\n')

        self.lines = ['']

        self.scrollY = 0
        self.scrollX = 0

        self.lastX = 0

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
        self.log.write(f'length: {len(text)}')
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
            'return': self.keyReturn,
            'delete': self.keyDelete,
            'down': self.keyDown,
            'up': self.keyUp,
            'left': self.keyLeft,
            'right': self.keyRight
        }
        
        if k == 'return':
            self.keyReturn()

        elif k == 'delete':
            self.keyDelete()

        if type(k) == int and k < 256:
            self.key(k)

        if k == 'down':
            self.keyDown()

        if k == 'up':
            self.keyUp()

        if k == 'left':
            self.keyLeft()

        if k == 'right':
            self.keyRight()

    def key(self, k):
        try:
            char = bytearray([k]).decode()
        except UnicodeDecodeError:
            self.log.write('UnicodeDecodeError: ' + str(k) + '\n')
            return

        preSection = self.lines[self.y + self.scrollY][:(self.x + self.scrollX)]
        postSection = self.lines[self.y + self.scrollY][(self.x + self.scrollX):]

        self.lines[self.y + self.scrollY] = preSection + char + postSection            

        self.updateScreen()

        self.keyRight()


    def keyReturn(self):
        pre = self.lines[self.y + self.scrollY][:self.x + self.scrollX] # current line
        post = self.lines[self.y + self.scrollY][self.x + self.scrollX:]

        self.lines[self.y + self.scrollY] = pre
        self.lines.insert(self.y + self.scrollY + 1, post)

        self.keyRight()

        self.updateScreen()


    def keyDelete(self):
        if self.x + self.scrollX > 0:
            preSection = self.lines[self.y + self.scrollY][:(self.x + self.scrollX) - 1]
            postSection = self.lines[self.y + self.scrollY][(self.x + self.scrollX):]

            self.lines[self.y + self.scrollY] = preSection + postSection
            self.x -= 1

            if self.scrollX > 0:
                maxWidth = self.scrollX + self.width
                visibleLines = self.lines[self.scrollY:self.scrollY + self.height]

                self.log.write(str(visibleLines) + '\n')

                if not any([len(line) >= maxWidth for line in visibleLines]):
                    self.scrollX -= 1
                    self.x += 1

            self.updateScreen()

        elif self.y + self.scrollY > 0:
            # blank line
            remains = self.lines.pop(self.y + self.scrollY)

            length = len(self.lines[self.y + self.scrollY - 1])

            self.keyLeft()

            self.lines[self.y + self.scrollY] += remains

            self.updateScreen()

        self.lastX = self.x + self.scrollX


    def keyDown(self):
        if not self.y + self.scrollY < len(self.lines) - 1:
            return

        update = False

        if self.y < self.height - 1:
            self.y += 1
        else:
            self.scrollY += 1
            update = True

        self.bounds(update)


    def keyUp(self):
        if not self.y + self.scrollY > 0:
            return

        update = False

        if self.y > 0:
            self.y -= 1
        else: # the condition where scrollY = 0 and y = 0 is convered by the outer if statement
            self.scrollY -= 1
            update = True

        self.bounds(update)     


    def keyLeft(self):
        update = False

        if self.x + self.scrollX > 0:
            if self.x > 0:
                self.x -= 1
            else:
                self.scrollX -= 1
                update = True

        elif self.y + self.scrollY > 0:
            # last line
            if self.y > 0:
                self.y -= 1
            else: # the condition where scrollY = 0 and y = 0 is convered by the outer if statement
                self.scrollY -= 1
                update = True

            length = len(self.lines[self.y + self.scrollY])

            self.x = length - self.scrollX
            if self.x > self.width:
                self.x = self.width - 1
                self.scrollX = length - self.x
                update = True

        self.lastX = self.x + self.scrollX

        if update:
            self.updateScreen()


    def keyRight(self):
        length = len(self.lines[self.y + self.scrollY])
        
        if self.x + self.scrollX < length:
            if self.x < self.width - 1:
                self.x += 1
            else:
                self.scrollX += 1
                self.updateScreen()
        else:
            # next line
            self.x = 0
            self.scrollX = 0

            if self.y < self.height - 1:
                self.y += 1
            else:
                self.scrollY += 1

            self.updateScreen()

        self.lastX = self.x + self.scrollX


    def bounds(self, update):
        self.x = self.lastX - self.scrollX

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

        if update:
            self.updateScreen()


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