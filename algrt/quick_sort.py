import random
import timeit
import sys

def partition(arr):
    pivot = arr[random.randrange(len(arr))]
    left, right = [], []

    for a in arr:
        if pivot > a:
            left.append(a)
        elif pivot < a:
            right.append(a)


    return left, [pivot], right

arr = [50,115,203,512,125,111,25,95,45,23,32,659,55,123]

print(partition(arr))

