dp = [[0]*10 for i in range(1001)]
dp[1] = [1] * 10

n = int(input())

for i in range(2, n+1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][0:j+1])

res = 0
for i in range(10):
    res = res + dp[n][i]

print(res % 10007)