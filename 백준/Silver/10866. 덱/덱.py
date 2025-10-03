import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
deq = deque([])

for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push_front':
        deq.appendleft(int(cmd[1]))
        #print(f"deq: {deq}\n")
    elif cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
        #print(f"deq: {deq}\n")
    elif cmd[0] == 'pop_front':
        if not deq: print(-1)
        else:
            print(deq.popleft())
            #print(f"deq: {deq}\n")
    elif cmd[0] == 'pop_back':
        if not deq: print(-1)
        else:
            print(deq.pop())
            #print(f"deq: {deq}\n")
    elif cmd[0] == 'size':
        print(len(deq))
        #print(f"deq: {deq}\n")
    elif cmd[0] == 'empty':
            if not deq: print(1)
            elif deq: print(0)
    elif cmd[0] == 'front':
        if not deq: print(-1)
        else:
            print(deq[0])
            #print(f"deq: {deq}\n")
    elif cmd[0] == 'back':
        if not deq: print(-1)
        else:
            print(deq[-1])
            #print(f"deq: {deq}\n")