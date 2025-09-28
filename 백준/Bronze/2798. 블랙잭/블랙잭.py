import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))

max_sum = 0
for combo in combinations(cards, 3):
    s = sum(combo)
    if s > max_sum and s <= m :
        max_sum = s

print(max_sum)