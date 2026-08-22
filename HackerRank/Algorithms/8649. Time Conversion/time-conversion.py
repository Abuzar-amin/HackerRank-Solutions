#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time = s.split(':')
    if 'PM' in s:
        if time[0] == '12':
            return s.replace('PM','')
        hour = int(time[0])
        hour += 12
        return (str(hour)+':'+time[1]+':'+time[2]).replace('PM','')
        
    else:
        if time[0] == '12':
            return('00'+':'+time[1]+':'+time[2]).replace('AM','')
        else:
            return s.replace('AM','')
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
