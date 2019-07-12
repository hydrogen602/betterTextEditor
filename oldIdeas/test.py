
from shutil import get_terminal_size

t = get_terminal_size((0, 0))

# t.columns
# t.lines

import main

r = main.renderer()

r.print('hi\n1\n2\n3\n')
input()
r.clear()
r.print('yeet')