# method 1
import sys
n = int(input())

for line in sys.stdin:
    a, b = map(int, line.split(','))
    print(a+b)


# method 2
# for i in range(int(input())):
#     a, b = map(int, (input().split(',')))
#     print(a+b)