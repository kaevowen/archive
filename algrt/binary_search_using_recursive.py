def bs_r(arr, target,start, end):
    start = start
    end = end
    mid = (start+end)//2

    if target == arr[mid]:
        return f"find target! index : {mid}"

    elif target > arr[mid]:
        start = mid + 1
        return bs_r(arr, target, start, end)

    elif target < arr[mid]:
        end = mid - 1
        return bs_r(arr, target, start, end)

    else:
        return -1


arr = [1,4,9,16,25,36,49,64,81]
print(arr)
print(bs_r(arr, 49, 0, len(arr)))