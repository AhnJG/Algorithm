n = int(input())

dp = [[0] * 2 for i in range(n+1)]
dp[1] = [0, 1]

for i in range(2, n+1):
    for j in range(2):
        if j == 0:
            dp[i][0] = dp[i-1][0] + dp[i-1][1]
        elif j == 1:
            dp[i][1] = dp[i-1][0]
        
print(sum(dp[n]))