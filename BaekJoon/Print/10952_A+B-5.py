import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == 0: # 문제 조건 (0 < a,b < 10)
        break
    print(a+b)