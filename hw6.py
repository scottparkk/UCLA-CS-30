
# Read the homework description carefully!

def halveEvens(l):
    result = []
    for x in l:
        if x % 2 == 0:
            result = result + [x//2]
        else:
            result = result
    return result

#def helpers(o,l):
#    result = []
#    for x in range(len(l)):
#        if range(len(l)) % 2 == 0:
#            return result + [

#def splitEveryOther(l):
#    o = l
#    return helpers(o,l)

def splitEveryOther(l):
    result = [[],[]]
    for x in range(len(l)):
        if x%2 == 0:
            result[0] = result[0] + [l[x]]
        else:
            result[1] = result[1] + [l[x]]
    return result

def isSorted(l):
    result = True
    for x in range(len(l)):
        if x + 1 == len(l):
            return  True
        if l[x] > l[x+1]:
            return False
    return result

def dotProduct(l1,l2):
    result = []
    for x in range(len(l1)):
        result = result + [l1[x] * l2[x]]
    return sum(result)

def negate(l):
    result = []
    for x in l:
        s = []
        for i in x:
            s = s + [{'r': 255 - i['r'], 'g': 255 - i['g'], 'b': 255 - i['b']}]
        result = result + [s]
    return result


def helpera(n):
    result = []
    i = n
    while i != 0:
        i = i//10
        result = result + [[]]
    return result

def toDigitList(n):
    y = n
    return helperb(n,y)

def helperb(n,y):
    result = []
    for x in helpera(n):
        result =  [y%10] + result
        y = y //10
    return result

def digitalRootAndPersistence(n):
    i = n
    return helperd(n,i)

def helperd(n,i):
    result = 0
    times = 0
    while len(toDigitList(i))!= 1:
        result = result + sum(toDigitList(i))
        i = sum(toDigitList(i))
        times = times + 1
    return {'root': i, 'persistence': times}



    
