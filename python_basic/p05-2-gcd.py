#GCD(Greatest Common Divisor, 최대공약수)
#유클리드 방식 : gcd(a, b) = gcd(b, a%b)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(5, 15))
