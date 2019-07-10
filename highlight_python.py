from keyword import kwlist

def init(builtins):
    global colors

    colors = [
        #(['def'], 52, 'till', '('),
        (['self'], 209),
        (kwlist, 209),
        (dir(builtins), 52),
        ('=-+*%^&|></~', 161),
        ('#', 245, 'till', '\n'),
        ('\'\"', 11, 'till', '\'\"')
    ]

colors = None



f = open('debug.log', 'w')
f.write(str(colors))
f.close()

def getSpecial(c):
    if len(c) <= 2:
        return None
    else:
        return c[1:4]


def split(line):
    dividers = ' (){}[]=+-*^%|?&<>.,:;@/~#\'\"'
    
    ls = []
    latest = ''
    currentDividing = False

    for char in line: 
        if char in dividers:
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

    for k in ls:
        if special:
            newLs.append((k, special[0]))

            if k in special[2] and special[1] == 'till':
                # end of special
                special = None

            continue

        for c in colors:
            if k in c[0]:
                s = getSpecial(c)
                if s:
                    assert s[1] == 'till'
                    special = s

                newLs.append((k, c[1]))
                break
        else:
            newLs.append((k, 16))

    return newLs

if __name__ == '__main__':
    print(getColors('# t.columns'))
