# 자신보다 작은 값을 가지는 항목들 중에 최대의 dp값을 가지는 위치를 찾고 그 값을 dp에 현재 값을 더하여 dp에 넣는다

n = int(input())
data = [0] + list(map(int, input().split()))

dp = [0] * (n+1)
dp[1] = data[1]

for i in range(1, n+1):

    max_d = 0
    for j in range(1, i):
        if data[i] > data[j] and dp[j] > max_d:
            max_d = dp[j]
    
    dp[i] = max_d + data[i]

print(max(dp))