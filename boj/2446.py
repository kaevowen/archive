n = 5
k = n-1
pivot = (n+(n-1)) // 2

print(n, k, pivot)

for i in range(0, n):
	for j in range(0, n+(n-1)):
		if j >= pivot - k and j <= pivot + k :
			print("*", end='')
		else:
			print(" ", end='')
	
	if i == n-1 :
		break
	else :			
		print("")
		k+=1
