'''
Created on Mar 3, 2022
Last Edited on Mar 4, 2022
@author: Madueke Emmanuel
'''
# Falling Distance
from random import randint
def fallingDistance(t, g=9.8):
    d = (0.5 * g * t**2)
    return str(d) + ' meters.'
for time in range(1, 11):
    distance = fallingDistance(time)
    print('Time ->', time, 'Distance ->', distance)
# Kinetic Energy
def kineticEnergy(m, v):
    ke = (0.5 * m * v**2)
    return ke
energy = kineticEnergy(34, 90)
print(energy)
# Celsius Temperature Table
def celsius(f):
    c = (5 / 9) * (f - 32)
    return c
for f in range(0, 21):
    print('The equivalent of', f, 'Fahrenheit is', celsius(f), 'Celsius.')
# Coin Toss
def coinToss():
    coin_id = randint(1, 2)
    coin_value = 'head' if coin_id == 1 else 'tail'
    return coin_value
toss_number = 4
coin_list = []
for toss in range(1, toss_number+1):
    coin_list.append((toss, coinToss()))
print(coin_list)
# Present Value
def presentValue(f, r, n):
    i = r / 100
    p = f / (1+i)**n
    return p
print(presentValue(10000, 10, 10))
# future Value
def futureValue(p, i, t):
    '''Returns the future value of the principal
        p: Present Value
        i: Interest Rate
        t: years
    '''
    r = i / 100
    f = p * (1 + r)**t
    return f
print(futureValue(3855.432894295314, 10, 10))
# Lowest Score Drop
def getScore(x, y=[]):
    y.append(x)
    return y if 0 <= x <= 100 else None
getScore(45)
getScore(87)
getScore(65)
getScore(90)
getScore(65)
def calcAverage(limit, *numbers):
    '''
    Can take only two arguments, limits and numbers
    :limit must be an integer
    :numbers must be a tuple
    '''
    numbers_list = list(numbers)
    scores = []
    while len(scores) < limit:
        reference = numbers_list[0]
        for value in numbers_list:
            if value > reference:
                reference = value
        scores.append(reference)
        numbers_list.remove(reference)
    print(scores)
    # Defining inner function findLowest
    def findLowest():
        nonlocal numbers_list
        reference = numbers_list[0]
        index = 0
        for ind, value in enumerate(numbers_list):
            if value < reference:
                reference = value
                index = ind
        lowest = numbers_list.pop(index)
        return(lowest)
    num = 0
    dem = len(scores)
    for score in scores:
        num += score
    average = num / dem
    print(findLowest())
    return average
print(calcAverage(4, *(1, 2, 3, 4, 5, 6, 7, 8)))#'''*getScore(73)'''))