#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#

def weightedMean(X, W):
    # Write your code here
    sum_value=0
    sum_weights=0
    for i in range(n):
        sum_value= sum_value + vals[i]*weights[i]
        sum_weights= sum_weights +weights[i]
    weighted_mean=sum_value/sum_weights
    print(round(weighted_mean,1)) 
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weightedMean(vals, weights)
