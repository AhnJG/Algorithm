#최대값 구하기
def find_max(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if max_v < a[i]:
            max_v = a[i]

    return max_v

a = [1, 5, 4, 2, 3]
print(find_max(a))