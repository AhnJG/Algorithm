# method 1
# import sys
# n = int(input())
# m = list(map(int, sys.stdin.readline().split()))

# print(min(m), max(m))

# method 2
import sys
n, *m = map(int, sys.stdin.read().split())
print(min(m), max(m))