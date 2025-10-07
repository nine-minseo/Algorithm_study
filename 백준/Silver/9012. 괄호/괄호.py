import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())

for _ in range(n):
    test_data = input()

    idx = 0
    stack = []
    is_vps = True

    while idx < len(test_data):
        if test_data[idx] == '(':
            stack.append(test_data[idx])
            #print(f"1_idx: {idx}, test_data[idx]: {test_data[idx]}, stack: {stack}\n")
            idx += 1
        elif test_data[idx] == ')':
            if not stack:
                print("NO")
                is_vps = False
                break
            elif stack[-1] == '(':
                #print(f"2_idx: {idx}, test_data[idx]: {test_data[idx]}, stack: {stack}\n")
                stack.pop()
                idx += 1

    if not is_vps:
        continue
    elif stack:
        #print(f"4_idx: {idx}, test_data[idx]: {test_data[idx]}, stack: {stack}\n")
        print("NO")
    elif is_vps:
        print("YES")