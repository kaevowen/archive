N = int(input())
imap = [[0 for col in range(0, N)] for row in range(0,N)]

for i in range(0, N):
	for j, m in enumerate(map(int, input().split())):
		imap[i][j] = m
for k in range(0, N):
	for i in range(0, N):
		for j in range(0, N):
			if imap[i][k] and imap[k][j]:
				imap[i][j] = 1

for i in range(N):
	for j in range(N):
		print(f"{imap[i][j]}", end=' ')
	print()