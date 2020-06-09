import sys
n = int(input())

for _ in range(n):
    print(sum(map(int, sys.stdin.readline().split())))

    # a, b = (map(int, sys.stdin.readline().split()))
    # print(a+b)
    