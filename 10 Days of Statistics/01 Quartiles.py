#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    arr.sort()
    Q2 = statistics.median(arr)
    arr_low,arr_hi = [],[]
    for i in arr:
        if i < Q2:
            arr_low.append(i)
        elif i > Q2:
            arr_hi.append(i)
    Q1 = statistics.median(arr_low)
    Q3 = statistics.median(arr_hi)
    return int(Q1),int(Q2),int(Q3)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
