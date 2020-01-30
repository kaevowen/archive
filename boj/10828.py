import sys 
import collections 
stack = collections.deque() 
n = int(sys.stdin.readline().strip()) 

for _ in range(n): 
    cmd = sys.stdin.readline().strip() 
    if cmd[:2] == "pu": 
        num = int(cmd.split(' ')[1]) 
        stack.append(num) 
    if cmd[:2] == "po": 
        if not stack: 
            print(-1) 
            continue 
        print(stack.pop()) 

    if cmd[0] == 's': 
        print(len(stack)) 

    if cmd[0] == 'e': 
        if stack: 
            print(0) 
            continue 
        print(1) 
    if cmd[0] == 't': 
        if not stack: 
            print(-1) 
            continue 
        print(stack[-1])
