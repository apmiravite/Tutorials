#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    bin_n=format(n,"b")
    x=[int(i) for i in str(bin_n)]
    
    highest=0
    count=0
    
    for i in range(0,len(x)):
        if x[i]==0:
            count=0
        else:
            count=count+1
            highest=max(count, highest)
    
    print(highest)
