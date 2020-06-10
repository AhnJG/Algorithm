# Ref https://j2wooooo.tistory.com/60
import sys

c, *n = map(int, sys.stdin.read().split())

dp = {1:1, 2:2, 3:4, 4:7}
def find(n):
    if n in dp:
        return dp[n]
    
    m = find(n-1) + find(n-2) + find(n-3)
    dp[n] = m
    
    return m

for i in range(c):
    print(find(n[i]))