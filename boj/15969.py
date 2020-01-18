ppl = int(input())
scores = list(map(int, input().split()))
scores.sort()
subs = scores[-1] - scores[0]
print(subs)
