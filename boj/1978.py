from math import sqrt, ceil
def pnum(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2, ceil(sqrt(n))):
        if n%i==0:
            return 0

    return 1


i = input()
j = list(map(int, input().split()))
cnt = 0
for J in j:
    if pnum(J):
        cnt+=1
print(cnt)