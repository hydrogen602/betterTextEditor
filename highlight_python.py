from keyword import kwlist

builtins = [
    'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
    'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
    'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
    'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 
    'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
    'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 
    'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
    'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 
    'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 
    'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 
    'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 
    'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 
    'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 
    'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 
    'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 
    'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 
    'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 
    'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 
    'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', 
    '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 
    'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
    'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 
    'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 
    'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 
    'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 
    'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 
    'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 
    'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 
    'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
    ]

def init(builtins):
    global colors

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
        ('\'\"', 11, 'till', '\'\"')
    ]

colors = None

init(builtins)




f = open('debug.log', 'w')
# f.write(str(colors))
f.close()

def getSpecial(c):
    if len(c) <= 2:
        return None
    else:
        return c[1:4]


def split(line):
    dividers = ' 1234567890(){}[]=+-*^%|?&<>.,:;@/~#\'\"'
    
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

def getColors(line):
    ls = split(line)
    newLs = []

    special = None

    # f = open('debug.log', 'a')

    t = colors[4][0]
    # f.write(f'update = {t}\n')

    for k in ls:
        if special:
            type_ = special[1]
            color = special[0]

            # if type_ != 'between':
            #     newLs.append((k, special[0]))

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

        for c in colors:
            if k in c[0]:
                s = getSpecial(c)
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

if __name__ == '__main__':
    print(getColors('# t.columns'))
