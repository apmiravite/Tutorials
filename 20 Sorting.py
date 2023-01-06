#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps=0
    temp=0
    firstElement=0
    lastElement=0
    iteration = 0
    while iteration<n:
        for i in range(n-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                numSwaps+=1
        iteration+=1
    firstElement=a[0]
    lastElement=a[n-1]
    print("Array is sorted in",numSwaps,"swaps.")
    print("First Element:",firstElement)
    print("Last Element:",lastElement)
