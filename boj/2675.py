t = int(input())

for _ in range(t):
    s = input().split()
    l, w = int(s[0]), s[1]

    for _ in range(l):
        a = ''
        for W in w:
            a = a + W * l

    print(a)