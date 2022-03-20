# help from Chloe Tsai Office Hours (GOD BLESS CHLOE)
# a few problems will use functions from this library
import math
#----------------------------------------------------------------------
# A TOTAL SECONDS
def hoursToSeconds(hours):
    return hours*3600
def minutesToSeconds(minutes):
    return minutes*60

def totalSeconds(hours, minutes, seconds):
    return hoursToSeconds(hours)+ minutesToSeconds(minutes) + seconds
#-----------------------------------------------------------------------

# B write the function relativelyPrime
# maybe use math.lcm, nope didnt work
#OMG there is a greatest common divisor

def relativelyPrime(integer1,integer2):
    
    return math.gcd(integer1,integer2) == 1

#-----------------------------------------------------------------------
# C write the function distanceFromSquare
#possibly use math.isqrt

def distanceFromSquare(x):
    sqrt= math.isqrt(x)
    square = sqrt*sqrt
    distance = x - square
    one= sqrt + 1
    big= one*one
    distance2= big - x
    return min(distance,distance2)
    
   
#-----------------------------------------------------------------------
# D write the function palindrome4

def palindrome4(word):
    return word[0]==word[3] and word[1]==word[2]

#-----------------------------------------------------------------------
# E write the function palindrome8

#WHAT I WANT TO DO IS.... MAke a list of [0,1,6,7] and [2,3,4,5] and apply
#the thing for palindrome4... hmmmmmmmmmmmmm
#tHE ONE I WROTE DOESNT WORK WITH LISTS UGHHH

def palindrome8(word):
   # hi= palindrome4(word[0]+word[1]+word[6]+word[7])
   # bye= palindrome4(word[2]+word[3]+word[4]+word[5])
   # return hi and bye
   hi = palindrome4([word[0]]+[word[1]]+[word[6]]+[word[7]])
   bye = palindrome4([word[2]]+[word[3]]+[word[4]]+[word[5]])
   return hi and bye
# HOW DID THAT WORKKKK LMAOOOOOOOOOO 

        
