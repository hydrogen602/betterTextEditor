
from menu import main


m = main()

f = open('info.log', 'w')

class checkable:

    def __init__(self, name, value=False):
        self.name = name
        self.value = value
    
    def setY(self, y):
        self.y = y
        f.write('self.y = {}\n'.format(y))

    def toggle(self, _):
        self.value = not self.value
        global m
                
        if self.value:
            m.window.addstr(self.y, 1, 'X')
        else:
            m.window.addstr(self.y, 1, ' ')

    def generate(self):
        global m
        m.window.addstr(self.y, 0, '[ ] - {}'.format(self.name))
        if m.isRunning:
            index = -1
        else:
            index = None
        m.addBox(self.y, 1, self.toggle, lim=0, index=index)

        if self.value:
            m.window.addstr(self.y, 1, 'X')
        

checklist = [
    checkable('task 1', True),
    checkable('task 2', False),
    checkable('task 3', False)
]

startY = 3
i = 0
for k in checklist:
    k.setY(startY + i)

    k.generate()

    i += 1

lowestY = startY + i

newBox = None

def newTask(name):
    if type(name) == bytearray:
        name = name.decode()
    global newBox, lowestY
    m.boxes.remove(newBox)
    m.window.addstr(newBox['y'], 0, ' ' * 30)
    assert newBox['y'] == lowestY
    f.write('lowestY = {}\n'.format(lowestY))
    
    c = checkable(name)
    c.setY(lowestY)
    c.generate()

    f.write('lowestY = {}\n'.format(lowestY))
    f.write('c.y = {}\n'.format(c.y))

    lowestY += 1
    checklist.append(c)

    newTaskBox(lowestY)
    
    f.write('m.boxes = {}\n'.format(m.boxes))

    

def newTaskBox(y):
    global newBox
    l = 'new task: '
    if m.isRunning:
        index = -1
    else:
        index = None
    newBox = m.addBox(y, len(l), func=newTask, lim=20, index=index)
    m.window.addstr(y, 0, l)

newTaskBox(lowestY)


#m.window.addstr(7, 1, str(m.boxes))

try:
    m.run()
finally:
    f.close()