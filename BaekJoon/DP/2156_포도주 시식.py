# Ref https://rebas.kr/836
import sys

n = int(sys.stdin.readline())
data = [0] + [int(sys.stdin.readline()) for _ in range(n)] + [0]

dp = [0] * (n+2)
dp[1], dp[2] = data[1], data[1] + data[2]

for i in range(3, n+1):
    x = dp[i-1] # 연속 0
    y = dp[i-2] + data[i] # 연속 1
    z = dp[i-3]+ data[i-1] + data[i]# 연속 2
    dp[i] = max(x, y, z)

print(dp[n])