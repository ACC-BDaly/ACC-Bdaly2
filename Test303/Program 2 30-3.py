'''Program 2:'''

import math

height = float(input('Height Input : '))
radius = float(input('Radius Input : '))

def volume(r, h):
    answer = math.pi*(r*r)*h
    return answer

print(volume(radius, height))
