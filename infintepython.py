'''

'''

import string
import random

shakespeare = "methinks it is like a weasel"

def make_string(best_guess):
    '''create a string from aplphabet if solution not found for index'''
    choices = string.ascii_lowercase + " "
    current_best = [i for i in best_guess]
    for i in range(len(current_best)):
        if current_best[i] == "*":
            current_best[i] = random.choice(choices)
    # return ''.join(random.choice(choices) for x in range(28))
    return ''.join(current_best)
       
def rate_string(some_str):
    '''rate current string and reset character if no match'''
    # current = [i for i in attempt]
    score = 0
    rate_this = [i for i in some_str]
    for i in range(len(rate_this)):
        if rate_this[i] == shakespeare[i]:
            score += 1
        else:
            rate_this[i] = "*"
    rated = ''.join(rate_this)
    return rated, score

def caller(goal):
    '''call make_string and rate_string until solution found'''
    str_guess = ""
    count = 0
    best = 0
    best_guess = "*" * len(goal)
    while goal != best_guess:
        str_guess = make_string(best_guess)
        score = rate_string(str_guess)[1]
        count += 1
        if score > best:
            best_guess = rate_string(str_guess)[0]
            best = score
            print(str_guess, score)
    print "it took {} iterations to find the solution".format(count)

caller(shakespeare)
    
