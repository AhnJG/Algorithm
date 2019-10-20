#조세퍼스 문제
n, m = map(int, input().split(' '))
a = [_ for _ in range(1, n+1)]
index = 0
print('<', end='')
while a:
    index = (index + m - 1) % len(a)
    print(a.pop(index), end='')
    if len(a) == 0:
        print('', end='')
    else:
        print(', ', end='')
print('>')