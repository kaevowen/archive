def counting_sort(values, k):
    #make list using a length
    b = [-1] * len(values)
    #make list using a's max value
    count = [0] * (k+1)
    #count numbers
    for i in values:
        count[i] += 1

    for i in range(k):
        count[i+1] += count[i]

    for i in reversed(range(len(values))):
        b[count[values[i]] - 1] = values[i]
        count[values[i]] -= 1

    return b


a=[5,2,4,6,2,1,5,5,4,4,2,3,1,0,100000]
print(counting_sort(a,max(a)))