#RESOURCES
#- googled the meaning of concatenate
#- Chloe Office Hours


#PROBLEM #1: Miscellaneous


# used in the last part of the homework assignment
import turtle
#------------------------------------------------------------------------------
#FIZZBUZZ
# I CANT FIGURE OUT HOW TO DO THE WHEN l IS DIVISBLE BY BOTH 3 AND 5
# TO RETURN l AGHHHHHHH

def fizzBuzz(n):
    if n%15==0:
        result = 'fizz buzz'
    elif n%5==0:
        result = 'buzz'
    elif n%3==0:
        result='fizz'
    else:
        result=n
    return result


#------------------------------------------------------------------------------
# ROCK PAPER SCISSORSSSZZZZ
def rps(player1,player2):
    sceneOne= (player1 == 'rock' and player2== 'paper')
    sceneTwo= (player1=='rock'  and player2=='scissors')
    sceneThree= (player1=='rock'  and player2=='rock' )
    sceneFour=(player1=='paper'  and player2== 'paper')
    sceneFive=(player1=='paper'  and player2=='scissors' )
    sceneSix=(player1=='paper'  and player2=='rock' )
    sceneSeven=(player1=='scissors'  and player2=='paper' )
    sceneEight=(player1=='scissors'  and player2=='scissors' )
    sceneNine=(player1=='scissors'  and player2== 'rock')
    if sceneOne:
        return 'player 2 wins'
    if sceneTwo:
        return 'player 1 wins'
    if sceneThree:
        return 'tie game'
    if sceneFour:
        return 'tiegame'
    if sceneFive:
        return 'player 2 wins'
    if sceneSix:
        return 'player 1 wins'
    if sceneSeven:
        return 'player 1 wins'
    if sceneEight:
        return 'tie game'
    if sceneNine:
        return 'player 2 wins'

#------------------------------------------------------------------------------
#COUNTDA POSITIVE INTEGERS

def countPos(l):
    
    if l == []:
        return 0
    else:
        head=l[0]
        tail=l[1:]
        if head > 0:
            result= 1 + countPos(tail)
        else:
            result= countPos(tail)
        return result
#-------------------------------------------------------------------------------
#THRESHOLD
    #BRUH WHY ISNT IT WORKING
    #lmao i put threshold(l,n) instead of threshold(tail,n) in the return
    

def threshold(l,n):
    if l == []:
        return []
    else:
        head= l[0]
        tail= l[1:]
        if n > head:
            return [n] + threshold(tail,n)
        else:
            return [head] + threshold(tail,n)

#-------------------------------------------------------------------------------

# INTEGER RANGE (FIX)

def intRange(low,high):
    l= [low]
    if  l == []:
        return []
    elif low == high:
        return []
    else:
        head= l[0]
        plusOne = head + 1
        
        return [head] + intRange(plusOne,high)

        
        
    
#-------------------------------------------------------------------------------
#Inner Lists

def innerLists(l):
    if l == []:
        return []
    else:
        head=l[0]
        tail=l[1:]
        tailResult= innerLists(tail)
        fun= intRange(1,head+1)
        if head < 1:
            return [[]] + tailResult
        else:
            return [fun] + tailResult
#===============================================================================
#Problem #2: Recursive Art

#A) Regular Polygon 
def helper(angle,n,sideLength):
    
    if n==0:
        return
    else:
        head=n
        tail= n-1
        turtle.forward(sideLength)
        print('forward the sidelength')
        turtle.left(angle)
        print('turn')
        return helper(angle,tail,sideLength)
        
    
def regularNGon(n,sideLength):
    angle= 360/n
    return helper(angle,n,sideLength)
#HOLY SH*T, F*CK YES OMG IM SO HAPPY OMG OMG I DID IT
#------------------------------------------------------------------------------

#B) Archimedean Spiral
def archSpiral(length,increment,angle,n):
    if n == 0:
        return
    else:
        head=n
        tail= n-1
        newLength= length+ increment
        turtle.forward(length)
        turtle.left(angle)
        return archSpiral(newLength,increment,angle,tail)
        
# that was easier than expected
#------------------------------------------------------------------------------
#C)Logarithmic Spiral
def logSpiral(length,percentIncrease,angle,n):
    if n == 0:
        return
    else:
        head=n
        tail=n-1
        newLength= length*(1+ (percentIncrease/100))
        turtle.forward(length)
        turtle.left(angle)
        return logSpiral(newLength,percentIncrease,angle,tail)
    
