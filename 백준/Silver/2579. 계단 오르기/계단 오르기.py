import sys
input = lambda: sys.stdin.readline().strip()

steps = [0] * 301
dp = [[0] * 3 for _ in range(301)]

steps_num = int(input())

for i in range(1, steps_num + 1):
    steps[i] = int(input())

if steps_num == 1:
    print(steps[1])
    sys.exit()

dp[1][1] = steps[1]
dp[1][2] = 0
dp[2][1] = steps[2]
dp[2][2] = steps[1] + steps[2]

for i in range(3, steps_num + 1):
    dp[i][1] = max(dp[i-2][1], dp[i-2][2]) + steps[i]
    dp[i][2] = dp[i-1][1] + steps[i]

print(max(dp[steps_num][1], dp[steps_num][2]))
