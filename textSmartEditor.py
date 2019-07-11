import time
import sys
from textEditor import TextEditor
from core import curses

# import completion

raise Exception

class TextSmartEditor(TextEditor):
    '''
    option-o to write out
    option-q to quit
    '''

    def __init__(self):
        super(TextSmartEditor, self).__init__()

        self.marginRight = self.width // 2

    def updateDim(self):
        super(TextSmartEditor, self).updateDim()
        
        self.width -= self.marginRight

    def checkErrors(self):
        code = '\n'.join(self.lines)
        try:
            exec(code)
        except Exception as e:
                return e # type(e).__name__, e.__traceback__.tb_lineno

        return

    def updateScreen(self, endLine=True):
        super(TextSmartEditor, self).updateScreen(endLine=endLine)

        start = self.width + self.getMargin()

        for y in range(self.height):
            # space available = (self.marginRight - 2)
            # msg = str(completion.understandLine(self.lines[y + self.scrollY]))

            msg = str(self.checkErrors())

            msg = msg[:self.marginRight - 2]

            text = '| ' + msg

            self.window.addstr(y, start, text, curses.color_pair(0))


        if not endLine:
            return

        #self.print(, self.height - 1, resetX=True, fullLine=True)
        msg1 = '<< option-q to quit >>'
        msg2 = '<< option-o to save >>'

        buf = '-' * ((self.width + self.marginLeft + self.marginRight) - len(msg1) - len(msg2) - 1)

        if buf == '':
            raise Exception('Make your window bigger (wider)')

        text = msg1 + buf + msg2

        self.window.addstr(self.height, 0, text, curses.color_pair(0)) # 16




if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: TextEditor file')
        sys.exit(1)

    # if not os.path.isfile(sys.argv[1]):
    #     print('error: file not found')
    #     sys.exit(1)


    with TextSmartEditor() as m:
        m.load(sys.argv[1])
        m.run()