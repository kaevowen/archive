from datetime import timedelta as td

t1 = list(map(int, input().split()))
t1 = td(hours=t1[0], minutes=t1[1])
t2 = td(minutes=45)
t3 = t1-t2

m, s = divmod(t3.seconds, 60)
h, m = divmod(m, 60)

print(h, m)