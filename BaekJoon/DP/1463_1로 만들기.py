dp = {1:0, 2:1}

def find(n):
    if n in dp:
        return dp[n]
    
    x = find(n//2) + n%2
    y = find(n//3) + n%3
    
    m = 1 + min(x, y)
    dp[n] = m
    return m

n = int(input())
print(find(n))