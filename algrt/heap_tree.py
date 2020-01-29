def Cre_heap(arr, key, i):
	arr[key] = i;
	while key>1:
		print(arr)
		if arr[key] < arr[key//2]:
			arr[key], arr[key//2] = arr[key//2], arr[key]
			key /= 2
		else:
			break




node = [1,2,3,4,5,6]

Cre_heap(node, 5, 6)


print(node)