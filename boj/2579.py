n = int(input())
stair = []
dp = []
for i in range(n):
    stair.append(int(input()))




dp.append(stair[0])
dp.append(stair[1] + stair[0])
dp.append(max(stair[2] + stair[0], stair[2] + stair[1]))

for n in range(3, n):
    dp.append(max(stair[n-2] + stair[n], dp[n-3] + stair[n-1] + stair[n]))

print(dp)

'''
6       
10      1
20      2
15      
25      1
10      
20      1
'''