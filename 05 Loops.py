#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    i=0
    for i in range(10):
        print(str(n)+" x "+ str(i+1) +" = "+str((i+1)*n))
