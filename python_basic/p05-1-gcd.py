#GCD(Greatest Common Divisor, 최대공약수)
def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i = i-1

print(gcd(60, 18))
