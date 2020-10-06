#!/bin/python3
# Day 7: Arrays
import math
import os
import random
import re
import sys

def myReverse(arr):
    newArr = []
    for i in range(len(arr)-1,-1, -1):
        newArr.append(str(arr[i]))
    return newArr

if __name__ == '__main__':
    try:
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        revArr = myReverse(arr)
        print(' '.join(item for item in revArr))
    except:
        print("Something went wrong.")