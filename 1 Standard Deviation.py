#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean=float(sum(arr)/n)
    sods=0.0
    for i in range(n):
        sods=sods + (float(arr[i])-mean)**2
    sd=round((sods/n)**(1/2),1)
    print(sd)
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
