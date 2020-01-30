import sys 
import collections 

queue = collections.deque() 
n = int(sys.stdin.readline().strip()) 

for _ in range(n): 
    cmd = sys.stdin.readline().strip() 
    if cmd[:6] == "push_f": 
        num = int(cmd.split(' ')[1]) 
        queue.append(num)

    if cmd[:6] == "push_b": 
        num = int(cmd.split(' ')[1]) 
        queue.appendleft(num) 

    if cmd[:5] == "pop_f": 
        if not queue: 
            print(-1) 
            continue 
        print(queue.pop()) 

    if cmd[:5] == "pop_b": 
        if not queue: 
            print(-1) 
            continue 
        print(queue.popleft()) 


    if cmd[0] == 's': 
        print(len(queue)) 

    if cmd[0] == 'e': 
        if queue: 
            print(0) 
            continue 
        print(1) 

    if cmd[0] == 'f': 
        if not queue: 
            print(-1) 
            continue 
        print(queue[-1])

    if cmd[0] == 'b': 
        if not queue: 
            print(-1) 
            continue 
        print(queue[0])
