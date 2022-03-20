import functools

#def toUpper(x):
#    
#    if ord(x) < 95:
#        return x
#    else:
#        return chr(ord(x) - 32)
def toUpper(c):
    if ord(c) > 90:
        return chr(ord(c)- 32)
    else:
        return c

def toLower(c):
    if ord(c) < 90:
        return chr(ord(c) + 32)
    else:
        return c

def allLower(l):
    return functools.reduce(lambda x, elem:x + elem,list(map(lambda x:toLower(x),l)))

def capitalize(l):
    inner = allLower(l)
    return toUpper(inner[0]) + inner[1:]
def title(l):
    return [capitalize(l[0])] + functools.reduce(lambda x, elem: x + [capitalize(elem)] if len(elem) > 3 else x + [allLower(elem)],l[1:],[])


    
def whileloop(W):
    r = 0
    i = 0
    while i < len(W):
        r += ord(W[i])
        i = i + 1
    return r
        
