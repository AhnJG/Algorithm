# BOJ 10951_A_B-4
# Ref https://bnzn2426.tistory.com/105

# method 1
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a+b)

# method 2
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break