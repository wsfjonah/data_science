#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'maximumOccurringCharacter' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts STRING text as parameter.
#

def maximumOccurringCharacter(text):
    sort_table = {}
    max_key = None
    max_count = 0
    for t in text:
        count = 0
        if t in sort_table:
            count = sort_table[t]
        count = count + 1
        sort_table[t] = count
        if max_count < count:
            max_key = t
            max_count = count
    return max_key



if __name__ == '__main__':

    text = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzAAAAA12321222222222'

    result = maximumOccurringCharacter(text)

    print(str(result) + '\n')
