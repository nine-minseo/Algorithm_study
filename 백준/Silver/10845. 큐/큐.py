import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
queue = deque([])

for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
        #print(f"queue: {queue}\n")
    elif cmd[0] == 'pop':
        if not queue: print(-1)
        else:
            print(queue.popleft())
            #print(f"queue: {queue}\n")
    elif cmd[0] == 'size':
        print(len(queue))
        #print(f"queue: {queue}\n")
    elif cmd[0] == 'empty':
            if not queue: print(1)
            elif queue: print(0)
    elif cmd[0] == 'front':
        if not queue: print(-1)
        else:
            print(queue[0])
            #print(f"queue: {queue}\n")
    elif cmd[0] == 'back':
        if not queue: print(-1)
        else:
            print(queue[-1])
            #print(f"queue: {queue}\n")