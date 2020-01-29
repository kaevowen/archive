import sys

def sort(arr):
    if len(arr) <= 0:
        return arr

    pivot = arr[len(arr)//2]
    left = []
    right = []

    for i in arr:
        if i > pivot:
            right.append(i)

        elif i < pivot:
            left.append(i)

    return sort(left) + [pivot] + sort(right)