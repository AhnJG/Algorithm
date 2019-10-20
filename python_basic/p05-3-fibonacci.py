#피보나치 수열
#0, 1, 1, 2, 3, 5, 8, ...
def fibo(n, s1, s2):
    if n == 0:
        return s1
    return fibo(n-1, s2, s1+s2)

print(fibo(6, 0, 1))
