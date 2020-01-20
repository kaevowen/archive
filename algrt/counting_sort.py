def counting_sort(values, k):
    #make list using a length
    b = [-1] * len(values)
    #make list using a's max value
    count = [0] * (k+1)
    #count numbers
    for i in values:
        count[i] += 1

    for i in range(max(value)):
        count[i+1] += count[i]

    for i in reversed(range(len(values))):
        b[count[values[i]] - 1] = A[i]
        count[values[i]] -= 1

    return b
