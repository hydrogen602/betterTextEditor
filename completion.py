
def getter(module):
    if module not in locals():
        try:
            exec(f'import {module}')
        except ModuleNotFoundError:
            return 'ModuleNotFoundError'


    ls = dir(module)

    return ls

def startingWith(letter, module):
    ls = getter(module)

    return [i for i in ls if i.startswith(letter)]

def onePossibility(letter, module):
    ls = startingWith(letter, module)

    if len(ls) == 1:
        return ls[0]
    else:
        return None

class variableTracker:

    def __init__(self, name, value, annotation=None):
        self.name = name
        self.value = value
        self.annotation = annotation
    
    def getType(self):
        return type(self.value)

    def correctType(self):
        if self.annotation == None:
            return True # not specified thus any type is ok

        return self.annotation == self.getType() # must be changed for python4

    def __str__(self):
        return f'variableTracker(name={self.name}, ' \
            + f'value={self.value}, annotation={self.annotation})'

    def __repr__(self):
        if self.annotation == None:
            typeName = 'anyType'
        else:
            typeName = self.annotation.__name__

        return f'{typeName} {self.name} = {self.value}'




        

def understandLine(understandLine_line):
    #
    # long variable names are used to avoid two vars sharing a name
    # its so annoying reading the long var names
    #

    understandLine_pre = set(locals())

    try:
        exec(understandLine_line)
    except Exception as e:
        return 'Error', type(e).__name__

    understandLine_post = dict(locals())

    understandLine_diff = set(understandLine_post).difference(understandLine_pre)

    understandLine_diff.remove('understandLine_pre')

    understandLine_newVars = list(understandLine_diff)

    understandLine_newVarsTracker = []

    if '__annotations__' in understandLine_post:
        understandLine_annotations = understandLine_post['__annotations__']
    else:
        understandLine_annotations = {}

    for understandLine_k in understandLine_post:
        if understandLine_k in understandLine_newVars:
            # new variable
            understandLine_value = understandLine_post[understandLine_k]

            if understandLine_k in understandLine_annotations:
                understandLine_annotation = understandLine_annotations[understandLine_k]
            else:
                understandLine_annotation = None

            understandLine_newVarsTracker.append(variableTracker(
                                            understandLine_k, 
                                            understandLine_value,
                                            understandLine_annotation
                                            ))         



    return understandLine_newVarsTracker


if __name__ == '__main__':
    #print(startingWith('r', 'sys'))

    #print()

    u = understandLine('a = 1')
    print(u)

    for i in u:
        print(f'{i.name} -> {i.correctType()}')