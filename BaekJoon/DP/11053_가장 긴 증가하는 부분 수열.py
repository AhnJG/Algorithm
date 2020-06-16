# Ref https://pa-pico.tistory.com/83
import sys 

n = int(input())
data = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    max_dp = 0

    for j in range(0, i):
        if max_dp < dp[j] and data[i] > data[j]:
            max_dp = dp[j]
    
    dp[i] = max_dp + 1
    
print(max(dp))