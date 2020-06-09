# method 1
import sys

n = int(input())
line = sys.stdin.readline()

res = 0
for i in range(n):
    res = res + int(line[i])

print(res)


# short code
# input()
# print(sum(map(int, input())))