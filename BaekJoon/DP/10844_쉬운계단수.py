# -*- coding: utf-8 -*- 

dp = [[0]*10 for i in range(101)] # (101, 10)
dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 첫자리는 1~9

n = int(input())

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else: # 1 <= j <= 9
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    
sum = 0
for i in range(10):
    sum = sum + dp[n][i]

print(sum % 1000000000)