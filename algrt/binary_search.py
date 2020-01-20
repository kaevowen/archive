def bs(p, target):
    start = 0
    end = len(p) - 1

    while start <= end:
        mid = (start+end)//2
        print(mid)

        if target == p[mid]:
            return f"find target! index : {mid}"

        elif target > p[mid]:
            start=mid + 1

        else:
            end = mid - 1

    return -1
