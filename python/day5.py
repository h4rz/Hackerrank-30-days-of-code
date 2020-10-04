#!/bin/python3
# Day 5: Loops
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    if n < 2 or n > 20:
        print("Invalid no.")
    else:
        for i in range(1,11):
            print(str(n) + " x " + str(i) + " = " + str((n*i)))
