# 1부터 n까지 연속한 숫자의 제곱의 합
#계산 복잡도 : O(n)
def square_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i**2
    return s

print(square_sum(10))

# 1부터 n까지 연속한 숫자의 제곱의 합2
#계산 복잡도 : O(1)
def square_sum2(n):
    return n * (n+1) * (2*n+1) // 6
print(square_sum2(10))
