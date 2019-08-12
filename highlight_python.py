from keyword import kwlist


#
# start moving everything into
# the class so that things
# can be packed a bit better
#


# f = open('debug.log', 'w')
# # f.write(str(colors))
# f.close()


class HighlighterPython:

    builtins = [
        'ArithmeticError', 'AssertionError', 'AttributeError', 
        'BaseException', 'BlockingIOError', 'BrokenPipeError', 
        'BufferError', 'BytesWarning', 'ChildProcessError', 
        'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError',
        'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 
        'EnvironmentError', 'Exception', 'False', 'FileExistsError', 
        'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 
        'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 
        'IndentationError', 'IndexError', 'InterruptedError', 
        'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 
        'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 
        'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 
        'OSError', 'OverflowError', 'PendingDeprecationWarning', 
        'PermissionError', 'ProcessLookupError', 'RecursionError', 
        'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning',
        'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning',
        'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 
        'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
        'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
        'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 
        'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', 
        '__import__', '__loader__', '__name__', '__package__', '__spec__', 
        'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 
        'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
        'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 
        'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 
        'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 
        'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 
        'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct',
        'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 
        'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
        'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
        ]

    colors = [
        # (start tokens, color, type, end token)

        (['class'], 52, 'between', ':('),
        (['def'], 52, 'between', '('),
        (['self'], 209),
        (kwlist, 209),
        (builtins, 52),
        ('=-+*%^&|></~', 161),
        ('1234567890', 7),
        ('#', 245, 'till', '\n'),
        ('\"', 11, 'till', '\"'),
        ('\'', 11, 'till', '\'')
    ]


    def __init__(self, rules=None):
        if rules:
            self.rules = rules
        else:            
            self.rules = HighlighterPython.colors

        self.multiLineComment = None

        self.backslash = False

        self.backslashColor = 6


    def getSpecial(self, c):
        if len(c) <= 2:
            return None
        else:
            return c[1:4]


    def split(self, line):
        dividers = ' 1234567890(){}[]=+-*^%|?&<>.,:;@/~#\'\"\\'
        
        ls = []
        latest = ''
        currentDividing = False

        for char in line: 
            if char in dividers:
                if latest != '':
                    ls.append(latest)
                currentDividing = True
                latest = char
            else:
                if currentDividing:
                    currentDividing = False
                    ls.append(latest)
                    latest = ''

                latest += char

        ls.append(latest)
        return ls

    def getColors(self, line):
        ls = self.split(line)
        newLs = []

        special = None


        # f = open('debug.log', 'a')

        # t = self.rules[4][0]
        # f.write(f'update = {t}\n')

        last3 = []
        for k in ls:

            last3.append(k)
            if len(last3) > 3:
                last3.pop(0)

            if self.multiLineComment:
                # print(f'debug {last3} {special}')
                if ''.join(last3) == self.multiLineComment:
                    # print('end')
                    self.multiLineComment = None

                newLs.append((k, 11))
                continue

            # print(f'special {special} {k}')

            if special:
                type_ = special[1]
                color = special[0]

                # if type_ != 'between':
                #     newLs.append((k, special[0]))

                # char right after a backslash
                if self.backslash:
                    newLs.append((k, self.backslashColor))
                    self.backslash = False
                    continue

                # check for backslash in a string
                if k == '\\' and special == (11, 'till', '\'\"'):
                    newLs.append((k, self.backslashColor))
                    self.backslash = True
                    continue

                if k in special[2] and type_ in ['till', 'between']:
                    # end of special
                    # f.write(f'ending {special}\n')
                    special = None

                    if type_ != 'between':
                        newLs.append((k, color))
                        continue
                    else:
                        pass # between at the end (i.e. at the end token)
                else:
                    # not the end, i.e. middle section
                    newLs.append((k, color))
                    continue

            if ''.join(last3) in ['\'\'\'', '"""']: #11, 'till', '\'\"'
                # print('debug!')
                # print(last3)
                self.multiLineComment = ''.join(last3)
                special = None
                newLs.append((k, 11))
                continue

            for c in self.rules:
                if k in c[0]:
                    s = self.getSpecial(c)
                    if s:
                        assert s[1] in ['till', 'between']
                        special = s
                        # f.write(f'activating {c}, key = {k}\n')

                    if s and s[1] == 'between':
                        continue

                    newLs.append((k, c[1]))
                    break
            else:
                newLs.append((k, 16))

        # f.close()

        return newLs

    def getAllColors(self, lines):
        self.multiLineComment = None
        return [self.getColors(l) for l in lines]


if __name__ == '__main__':
    h = Highlighter()
    print(h.getColors(' t.column\'s\\a\' abc'))
