def quick_sort(v, start, end):
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1

    a[i], a[end] = a[end], a[i]
    quick_sort_acc(a, start, i-1)
    quick_sort_acc(a, i+1, end)

def quick_sort_acc(a):
    quick_sort(a, 0, len(a), len(a)-1)