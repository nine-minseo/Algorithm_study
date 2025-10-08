import sys
input = lambda: sys.stdin.readline().strip()

str = input()
stack = []
sum = 0
temp = 1
pre = ''
is_vps = True

for ch in str:
    #print(f"ch: {ch}")

    if ch == '(':
        temp *= 2
        #print(f"sum: {sum}, temp: {temp}\n")
        stack.append(ch)
        #print(f"stack: {stack}\n")
    elif ch == '[':
        temp *= 3
        #print(f"sum: {sum}, temp: {temp}\n")
        stack.append(ch)
        #print(f"stack: {stack}\n")
    elif ch == ')':
        if not stack or stack[-1] == '[':
            is_vps = False
            break
        elif stack[-1] == '(':
            stack.pop()
            #print(f"stack: {stack}")
            if pre == '(':
                sum += temp
            temp //= 2
            #print(f"sum: {sum}, temp: {temp}\n")
    elif ch == ']':
        if not stack or stack[-1] == '(':
            is_vps = False
            break
        elif stack[-1] == '[':
            stack.pop()
            #print(f"stack: {stack}")
            if pre == '[':
                sum += temp
            temp //= 3
            #print(f"sum: {sum}, temp: {temp}\n")
    pre = ch

if stack:
    is_vps = False

if is_vps:
    print(sum)
else:
    print(0)