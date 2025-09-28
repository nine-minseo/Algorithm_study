import sys
n, x = map(int, sys.stdin.readline().rstrip().split())

input_array = list(map(int, input().split()))

for i in input_array:
    if i < x:
        print(i, end=" ")