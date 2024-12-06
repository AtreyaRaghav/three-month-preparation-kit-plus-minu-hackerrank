#!/bin/python3

# Author Raghav Atreya
# 06-Dec-2024


import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # The function is easy to understand
    # O(n) is the complexity of the function
    
    number_of_pos_element = 0
    number_of_neg_element = 0
    number_of_zero_element = 0
    
    for element in arr:
        if element < 0:
            number_of_neg_element += 1
        elif element == 0:
            number_of_zero_element += 1
        else:
            number_of_pos_element += 1
    
    # len attribute has complexity of O(1)
    
    print(round(number_of_pos_element/len(arr) , 6)) 
    print(round(number_of_neg_element/len(arr), 6)) 
    print(round(number_of_zero_element/len(arr), 6))    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
