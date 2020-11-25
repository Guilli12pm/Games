import sys
import math

def round_down(n, decimals):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def summing(num,dec):
    print(num)

    odd = []
    even = []

    guess = 0
    iodd = 0
    ieven = 1

    while num != round_down(guess,dec):
        while guess < num:
            add = 1/(2*iodd+1)
            odd.append(add)
            guess += add
            iodd += 1
        print(guess)
        if num == round_down(guess,dec):
            break
        while guess > num:
            sub = 1/(2*ieven)
            even.append(sub)
            guess -= add
            ieven += 1
        if num == round_down(guess,dec):
            break
        print(guess)

    return iodd + ieven -1, len(odd), len(even)

print(summing(4.38,8))