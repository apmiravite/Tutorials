#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    arr=[]
    for i in range(len(values)):
        for j in range(freq[i]):
            arr.append(values[i])
    arr.sort()
    #print(arr)
    arr_low=[]
    for i in range(math.floor(len(arr)/2)):
        arr_low.append(arr[i])
    Q1=statistics.median(arr_low)
    #print(arr_low)
    #print(Q1)
    arr_hi=[]
    for i in range(math.ceil(len(arr)/2), len(arr)):
        arr_hi.append(arr[i])
    #print(arr_hi)
    Q3=statistics.median(arr_hi)
    #print(Q3)
    #print(Q3-Q1)
    print(format(Q3-Q1, '.1f'))
if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
