#!/bin/python3

# Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

    print(factorial(n))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
