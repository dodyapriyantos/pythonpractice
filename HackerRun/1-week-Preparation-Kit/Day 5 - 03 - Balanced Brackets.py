#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    
    stack_push_pop = ""
    
    for data in s:
        if (((data == ")") or (data == "}") or (data == "]")) and (stack_push_pop == "")) : return("NO")
        elif ((data == "(") or (data == "[") or (data == "{")) : stack_push_pop+=data
        elif ((data == ")") and (stack_push_pop[-1] != "(")): return("NO") 
        elif ((data == "}") and (stack_push_pop[-1] != "{")): return("NO") 
        elif ((data == "]") and (stack_push_pop[-1] != "[")): return("NO")
        else: stack_push_pop = stack_push_pop[:-1]
    
    if (len(stack_push_pop) != 0): return("NO")
    else: return("YES")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
