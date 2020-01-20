def bubble_sort(n, k):
    for i in range(k):
        for j in range(k-i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n


a = [5,4,8,7,4,5,6,2,3,10,9,1]
print(a)
print(bubble_sort(a, len(a)-1))