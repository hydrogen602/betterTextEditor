
import core

class TextRenderer(core.Main):
    """docstring for TextRenderer"""
    def __init__(self):
        super(TextRenderer, self).__init__()
        self.log.write('hi')

        self.lines = ['']

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

    def print(self, text, row, color=16):
        if row == len(self.lines):
            # new line
            self.lines.append('')
        prevText = self.lines[row]
        col = len(prevText)
        self.window.addstr(row, col, text, core.curses.color_pair(color))
        self.lines[row] = prevText + text

    def processKey(self, k):

        if k == 'return':
            pass
        elif k == 'delete':
            pass

        if type(k) == int and k < 256:
            self.__buf.append(k)
                
            self.window.addstr(self.y, self.x, bytearray([k]).decode())

            self.x += 1 # crashable

if __name__ == '__main__':
    with TextRenderer() as m:
        m.load('main.py')
        m.run()