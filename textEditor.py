
import textRenderer
import time

class TextEditor(textRenderer.TextRenderer):
    """docstring for TextEditor"""
    def __init__(self):
        super(TextEditor, self).__init__()

    def processKey(self, k):
        options = {
            'return': self.keyReturn,
            'delete': self.keyDelete,
            'down': self.keyDown,
            'up': self.keyUp,
            'left': self.keyLeft,
            'right': self.keyRight
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
        try:
            char = bytearray([k]).decode()
        except UnicodeDecodeError:
            self.log.write('UnicodeDecodeError: ' + str(k) + '\n')
            return

        preSection = self.lines[self.y + self.scrollY][:(self.x + self.scrollX)]
        postSection = self.lines[self.y + self.scrollY][(self.x + self.scrollX):]

        self.lines[self.y + self.scrollY] = preSection + char + postSection            

        self.keyRight()

        return True


    def keyReturn(self):
        pre = self.lines[self.y + self.scrollY][:self.x + self.scrollX] # current line
        post = self.lines[self.y + self.scrollY][self.x + self.scrollX:]

        self.lines[self.y + self.scrollY] = pre
        self.lines.insert(self.y + self.scrollY + 1, post)

        self.keyRight()

        return True


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

        elif self.y + self.scrollY > 0:
            # blank line
            remains = self.lines.pop(self.y + self.scrollY)

            length = len(self.lines[self.y + self.scrollY - 1])

            self.keyLeft()

            self.lines[self.y + self.scrollY] += remains

        self.lastX = self.x + self.scrollX

        return True


if __name__ == '__main__':
    with TextEditor() as m:
        m.load('TextEditor.py')
        m.run()


