
import core
import time

class TextRenderer(core.Main):
    """docstring for TextRenderer"""
    def __init__(self):
        super(TextRenderer, self).__init__()
        self.log.write('hi')

        self.lines = ['']

        self.scrollY = 0
        self.scrollX = 0

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
        #log.write(f'{self.m.height}')
        for i in range(self.height - 2):
            self.log.write(text[i] + '\n')
            self.print(text[i], i)

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

        self.window.addstr(row, col, text, core.curses.color_pair(color))
        if not resetX:
            self.lines[row] = prevText + text

    def processKey(self, k):

        if k == 'return':
            self.y += 1
            self.lines.insert(self.y, '')

            if self.y == self.height:
                self.y -= 1
                self.scrollY += 1

            self.x = 0
            self.scrollX = 0
            
            self.updateScreen()

        elif k == 'delete':
            if len(self.lines[self.y + self.scrollY]) > 0:
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
            else:
                # blank line
                self.lines.pop(self.y + self.scrollY)
                self.updateScreen()
                k = 'up'


        if type(k) == int and k < 256:
            try:
                char = bytearray([k]).decode()
            except UnicodeDecodeError:
                self.log.write('UnicodeDecodeError: ' + str(k) + '\n')
                return

            preSection = self.lines[self.y + self.scrollY][:(self.x + self.scrollX)]
            postSection = self.lines[self.y + self.scrollY][(self.x + self.scrollX):]

            self.lines[self.y + self.scrollY] = preSection + char + postSection            

            self.updateScreen()

            k = 'right'

        if k == 'down' and self.y + self.scrollY < len(self.lines) - 1:


            if self.y < self.height - 1:
                self.y += 1
            else:
                self.scrollY += 1
                self.updateScreen()

        if k == 'up' and self.y + self.scrollY > 0:
            self.log.write(f'up {self.y} {self.scrollY}\n')
            if self.y > 0:
                self.y -= 1
            else: # the condition where scrollY = 0 and y = 0 is convered by the outer if statement
                self.scrollY -= 1
                self.updateScreen()

        if k == 'left' and self.x + self.scrollX > 0:
            if self.x > 0:
                self.x -= 1
            else:
                self.scrollX -= 1
                self.updateScreen()

        if k == 'right':
            length = len(self.lines[self.y + self.scrollY])
            if self.x + self.scrollX < length:
                if self.x < self.width - 1:
                    self.x += 1
                else:
                    self.scrollX += 1
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