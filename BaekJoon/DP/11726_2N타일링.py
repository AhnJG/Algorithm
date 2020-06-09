# method 1
dp = {1:1, 2:2}

def find(n):
    if n in dp:
        return dp[n]
    
    m = find(n-1) + find(n-2)
    dp[n] = m
    return m

n = int(input())
print(find(n) % 10007)

# method 2
# n = int(input())
# a = b = 1
# for i in range(n):
#     a, b = b, a+b
# print(a%10007)