import sys

n = int(input())

def solve(col, cost, dp):
    dp[0][0], dp[1][0] = cost[0][0], cost[1][0]
    dp[0][1], dp[1][1] = dp[1][0] + cost[0][1], dp[0][0] + cost[1][1]
     
    for i in range(2, col):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + cost[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + cost[1][i]
    
    print(max(dp[0][col-1], dp[1][col-1]))

for i in range(n):
    col = int(input())
    cost = [[0] * col for i in range(2)] # (2, col)
    
    cost[0] = list(map(int, sys.stdin.readline().split()))
    cost[1] = list(map(int, sys.stdin.readline().split()))

    dp = [[0] * col for i in range(2)] # (2, col)

    solve(col, cost, dp)