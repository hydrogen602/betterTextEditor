
from core import Main, curses
import time

from highlight_python import HighlighterPython
from highlight_nasm import HighlighterNASM

# Idea: make it auto detect key methods using dir() and then run
# them using getattr()


class TextRenderer(Main):


    def __init__(self):
        super(TextRenderer, self).__init__()
        self.log.write('hi\n')

        self.lines = ['']

        self.scrollY = 0
        self.scrollX = 0

        self.lastX = 0

        self.lastKeyPress = { 'type': None, 'time': 0 }

        self.pathAndFile = None

        self.lengthOfFile = 0

        self.highlighter = HighlighterPython()

        self.unsavedContent = False # always false for this class
        # altered by edit-enabled subclasses

        self.prompt = None


    def getMargin(self):
        self.lengthOfFile = len(self.lines)
        self.marginLeft = 1 + len(str(self.lengthOfFile))
        return self.marginLeft


    def updateDim(self):
        self.height, self.width = self.window.getmaxyx()
        self.width -= self.getMargin()


    def load(self, pathAndFile):
        self.pathAndFile = pathAndFile

        text = None
        f = None
        try:
            f = open(pathAndFile)
            text = f.read()
        except FileNotFoundError as e:
            text = ''
        finally:
            if f:
                f.close()

        text = text.split('\n')

        self.log.write(f'loaded: {pathAndFile}\n')
        self.log.write(f'length: {len(text)}\n')

        if self.pathAndFile.endswith('.asm'):
            self.highlighter = HighlighterNASM()

        self.lines = []
        for line in text:
            self.lines.append(line)

        self.updateScreen()


    def preColorPrint(self, data, row, fullLine=True):
        # called for every row
        # data is entire row

        counter = 0

        inVisibleRegion = False

        offScreenLeft = 0

        breakNow = False

        for p in data:
            #self.log.write(f'p = {p}\n')

            txt = p[0]
            color = p[1]

            if len(txt) + offScreenLeft >= self.scrollX and not inVisibleRegion:
                inVisibleRegion = True
                
                txt = txt[self.scrollX - offScreenLeft:]

            if not inVisibleRegion:
                offScreenLeft += len(txt)
                continue

            # in visible region

            if len(txt) + counter >= self.width:
                txt = txt[:self.width - counter - 1]
                breakNow = True

            self.window.addstr(row, self.marginLeft + counter, txt, curses.color_pair(color))

            counter += len(txt)

            if breakNow:
                break

        if fullLine:
            filler = ' ' * (self.width - counter - 1)
            self.window.addstr(row, self.marginLeft + counter, filler, curses.color_pair(16))



    # def colorPrint(self, text, row, resetX=False, fullLine=False):
    #     if resetX: # start at the beginning of the line
    #         prevText = ''
    #         counter = 0
    #     else:
    #         prevText = self.lines[row]
    #         counter = len(prevText)

    #     if row == len(self.lines):
    #         # new line
    #         self.lines.append('')

    #     textColorPairs = highlight_python.getColors(text)

    #     breakNow = False

    #     for p in textColorPairs:
    #         txt = p[0]
    #         color = p[1]

    #         if counter + len(txt) >= self.width:
    #             # counter + len(txt) = self.width + 1
    #             txt = txt[:self.width - counter - 1]
    #             breakNow = True

    #         self.window.addstr(row, self.marginLeft + counter, txt, curses.color_pair(color))

    #         counter += len(txt)

    #         if breakNow:
    #             break

    #     if fullLine:
    #         filler = ' ' * (self.width - counter - 1)
    #         self.window.addstr(row, self.marginLeft + counter, filler, curses.color_pair(16))

    #     if not resetX:
    #         self.lines[row] = prevText + text



    # def print(self, text, row, color=16, resetX=False, fullLine=False):
    #     raise DeprecationWarning('not updated anymore')

    #     if resetX: # start at the beginning of the line
    #         prevText = ''
    #         col = resetX
    #     else:
    #         prevText = self.lines[row]
    #         col = len(prevText)

    #     if col + len(text) >= self.width:
    #         visibleText = text[:self.width - col - 1]
    #     else:
    #         visibleText = text

    #     self.window.addstr(row, col, visibleText, curses.color_pair(color))

    #     counter = col + len(visibleText)
    #     if fullLine:
    #         filler = ' ' * (self.width - counter - 1)
    #         self.window.addstr(row, counter, filler, curses.color_pair(16))

    #     if not resetX:
    #         self.lines[row] = prevText + text


    def createPrompt(self, prompt, longAnswer=False):
        row = (self.height - len(prompt)) // 2
        col = (self.width - len(prompt[0])) // 2

        for i in range(len(prompt)):
            self.window.addstr(row + i, col, prompt[i], curses.color_pair(0))

        self.window.move(0, self.marginLeft)

        ls = []
        while True:
            k = self.captureKey()

            if longAnswer and k == 'return':
                break

            try:
                answer = bytearray([k]).decode()
            except UnicodeDecodeError:
                self.log.write('UnicodeDecodeError: ' + str(k) + '\n')
            else:
                if longAnswer:
                    ls.append(answer)
                else:
                    break # success, got an answer

        return answer

    def close(self):
        # ask for save? in textEditor

        # for edit-enabled subclasses
        if self.unsavedContent:
            # ask for save
            prompt = [
                '+-------------------------------+',
                '|                               |',
                '|  Close without saving? (Y|N)  |',
                '|                               |',
                '+-------------------------------+'
                ]

            answer = self.createPrompt(prompt)

            if answer in ['Y', 'y']:
                pass # proceed closing

            elif answer in ['N', 'n']:
                # self.log.write('closing stopped \n')
                self.updateScreen()
                return

        # self.log.write(f'closing {answer} \n')
        self.isRunning = False


    def processKey(self, k):
        options = {
            'down': self.keyDown,
            'up': self.keyUp,
            'left': self.keyLeft,
            'right': self.keyRight,
            'opt-q': self.close
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


    def updateScreen(self, endLine=True):
        #self.window.erase()
        #self.window.refresh()

        #self.log.write(f'updating! {self.scrollY}\n')
        self.updateDim()

        # self.log.write(f'dimensions = {self.height} x {self.width}\n')

        margin = self.getMargin()

        linesColor = self.highlighter.getAllColors(self.lines)

        # for l in self.linesColor:
        #     self.log.write(str(l) + '\n')


        for y in range(self.height):
            if self.scrollY + y >= len(self.lines):
                break

            # entireLine = self.lines[self.scrollY + y]

            entireLineData = linesColor[self.scrollY + y]

            self.preColorPrint(entireLineData, y, fullLine=True)

            # visibleLine = entireLine[self.scrollX:self.scrollX + self.width]

            # self.colorPrint(visibleLine, y, resetX=margin, fullLine=True)



            lineNumber = y + self.scrollY + 1
            self.window.addstr(y, 0, f'{lineNumber:0{margin - 1}d}|', curses.color_pair(16))
            # self.log.write(f'adding line {lineNumber:0{margin - 1}d}| at {y}')


        if not endLine:
            return

        #self.print(, self.height - 1, resetX=True, fullLine=True)
        msg1 = '<< option-q to quit >>'
        msg2 = '<< option-o to save >>'

        buf = '-' * ((self.width + self.marginLeft) - len(msg1) - len(msg2) - 1)

        if buf == '':
            raise Exception('Make your window bigger (wider)')

        text = msg1 + buf + msg2

        self.window.addstr(self.height, 0, text, curses.color_pair(0)) # 16


if __name__ == '__main__':
    # prob doesnt work right now. use textEditor
    with TextRenderer() as m:
        m.load('main.py')
        m.run()


