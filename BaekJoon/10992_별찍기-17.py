n = int(input())

print(' '*(n-1)+'*')

if n != 1:
    for i in range(2, n):
        print(' '*(n-i) + '*' + ' '*((i-1)*2-1) + '*')

    print('*'*(2*n-1))