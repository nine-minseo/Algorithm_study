import sys

input = sys.stdin.readline

n = int(input().strip())
seq = list(map(int, input().strip().split()))
x = int(input().strip())

seq.sort()
#print(seq)
i, j = 0, len(seq) - 1

count = 0
while (i < j):
    #print(f"seq[i]: {seq[i]}, seq[j]: {seq[j]}")
    sum = seq[i] + seq[j]
    if x == (sum):
        count += 1
        #print(f"count: {count}")
        i += 1
        j -= 1
    elif sum < x:
        i += 1
    elif sum > x:
        j -= 1

print(count)