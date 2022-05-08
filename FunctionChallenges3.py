'''
Created on Mar 7, 2022
Last Edited on Mar 7, 2022
@author: Madueke Emmanuel
'''
# Star Search
def getJudgeData(x, y=[]):
    if 0 <= x <= 10:
        y.append(x)
        return y
    else:
        return 'Enter a valid number!'
def calcScore(*n):
    scores = list(n)
    def findLowest():
        nonlocal scores
        reference = scores[0]
        for l in scores:
            if l < reference:
                reference = l
        return reference
    def findHighest():
        nonlocal scores
        reference = scores[0]
        for h in scores:
            if h > reference:
                reference = h
        return reference
    lowest, highest = findLowest(), findHighest()
    print('The lowest score is ' + str(lowest) + '.' )
    print('The highest score is ' + str(highest) + '.' )
    num = 0
    for score in scores:
        if score in (lowest, highest):
            scores.remove(score)
        else:
            num+=score
    den = len(scores)
    average = num/den
    return 'Your average score is ' + str(average)
judge_1 = getJudgeData(9)
judge_2 = getJudgeData(6)
judge_3 = getJudgeData(8)
judge_4 = getJudgeData(3)
judge_5 = getJudgeData(10)
total = calcScore(*judge_5)
print(total)