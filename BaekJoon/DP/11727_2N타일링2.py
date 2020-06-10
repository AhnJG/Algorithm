dp = {1:1, 2:3}

def find(n):
    if n in dp:
        return dp[n]

    m = find(n-1) + 2 * find(n-2)
    dp[n] = m
    return m

n = int(input())
print(find(n) % 10007)