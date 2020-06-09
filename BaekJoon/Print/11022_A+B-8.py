import sys
n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())

    print('Case #%d: %d + %d = %d'%(i+1, a, b, a+b))