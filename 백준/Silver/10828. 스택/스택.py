import sys
input = sys.stdin.readline

n = int(input().strip())
stack = []

for _ in range(n):
    cmd = input().strip().split()
    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
        #print(f"stack: {stack}\n")
    elif cmd[0] == 'pop':
        if not stack: print(-1)
        else:
            print(stack.pop())
            #print(f"stack: {stack}\n")
    elif cmd[0] == 'size':
        print(len(stack))
        #print(f"stack: {stack}\n")
    elif cmd[0] == 'empty':
            if not stack: print(1)
            elif stack: print(0)
    elif cmd[0] == 'top':
        if not stack: print(-1)
        else:
            print(stack[-1])
            #print(f"stack: {stack}\n")