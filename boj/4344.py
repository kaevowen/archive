r = int(input())

for i in range(r):
    #ppl_avg[0] -> number of people
    #ppl_avg[1...] -> score

    a = list(map(int, input().split(' ')))

    avg = sum(a[1:]) / a[0]
    count = 0

    for i in a[1:]:
        if avg < i:
            count += 1

    print("%.3f" %round((count/a[0])*100, 3)+"%")