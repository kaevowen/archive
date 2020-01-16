string = input()
index = 0
for i in range(len(string)//10+1):
    print(string[index:index+10])
    index+=10
