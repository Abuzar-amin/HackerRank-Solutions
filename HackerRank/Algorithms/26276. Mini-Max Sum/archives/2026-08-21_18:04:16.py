#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minmax=[]
    min= 0
    max = 0
    arr.sort()
    for i in range(len(arr)-1):
        min += arr[i]
    for i in range(1,len(arr)):
        max += arr[i]
    minmax = [min, max]
    print(minmax[0], minmax[1])
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
