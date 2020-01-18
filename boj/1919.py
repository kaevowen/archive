f=[_ for _ in input()]
c=0

for _ in input():
    try:
        f.remove(_)
    except:
        c+=1

print(len(t)+c)