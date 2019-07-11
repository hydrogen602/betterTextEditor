
from textRenderer import TextRenderer
import time
import sys


class TextEditor(TextRenderer):
    '''
    option-o to write out
    option-q to quit
    '''

    def __init__(self):
        super(TextEditor, self).__init__()

        self.height -= 1

        self.unsavedContent = False


    def updateDim(self):
        self.height, self.width = self.window.getmaxyx()
        self.height -= 1
        self.width -= self.getMargin()


    def dump(self):
        if not self.pathAndFile:
            self.log.write('pathAndFile not specified yet\n')
            sys.exit(1)

        # prepare

        text = '\n'.join(self.lines)

        with open(self.pathAndFile, 'w') as f:
            f.write(text)

        self.unsavedContent = False

        return False


    def processKey(self, k):
        options = {
            'return': self.keyReturn,
            'delete': self.keyDelete,
            'down': self.keyDown,
            'up': self.keyUp,
            'left': self.keyLeft,
            'right': self.keyRight,
            'opt-o': self.dump,
            'opt-q': self.close
        }

        update = False

        if k in options:
            function = options[k]
            update = function()


        elif type(k) == int and k < 256:
            update = self.key(k)

        self.lastKeyPress['type'] = k
        self.lastKeyPress['time'] = time.time()

        if update:
            self.updateScreen()


    def key(self, k):
        self.unsavedContent = True

        try:
            char = bytearray([k]).decode()
        except UnicodeDecodeError:
            self.log.write('UnicodeDecodeError: ' + str(k) + '\n')
            return

        preSection = self.lines[self.y + self.scrollY][:(self.x + self.scrollX)]
        postSection = self.lines[self.y + self.scrollY][(self.x + self.scrollX):]

        if k == 9: # tab
            char = '    ' # four spaces

        self.lines[self.y + self.scrollY] = preSection + char + postSection            

        if k == 9:
            for _ in range(3):
                self.keyRight()

        self.keyRight()

        return True


    def keyReturn(self):
        self.unsavedContent = True

        pre = self.lines[self.y + self.scrollY][:self.x + self.scrollX] # current line
        post = self.lines[self.y + self.scrollY][self.x + self.scrollX:]

        self.lines[self.y + self.scrollY] = pre
        self.lines.insert(self.y + self.scrollY + 1, post)

        self.keyRight()

        return True


    def keyDelete(self):
        self.unsavedContent = True

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

        elif self.y + self.scrollY > 0:
            # blank line
            remains = self.lines.pop(self.y + self.scrollY)

            #length = len(self.lines[self.y + self.scrollY - 1])

            self.keyLeft()

            self.lines[self.y + self.scrollY] += remains

            if self.y + self.scrollY == len(self.lines) - 1:
                # last line
                self.window.erase()
                
                # erase() to cleanup leftovers

        self.lastX = self.x + self.scrollX

        return True


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: TextEditor file')
        sys.exit(1)

    # if not os.path.isfile(sys.argv[1]):
    #     print('error: file not found')
    #     sys.exit(1)


    with TextEditor() as m:
        m.load(sys.argv[1])
        m.run()


