#팩토리얼
def fact(n):
    s = 1
    for i in range(2, n+1):
        s *= i

    return s

print(fact(5))
