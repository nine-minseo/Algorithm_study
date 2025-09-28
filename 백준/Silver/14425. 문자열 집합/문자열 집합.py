import sys

input = sys.stdin.readline

n, m = map(int, input().split())
S = [input().strip() for _ in range(n)]
check = [input().strip() for _ in range(m)]

count = 0
for word in check:
    if word in S:
        count += 1

print(count)