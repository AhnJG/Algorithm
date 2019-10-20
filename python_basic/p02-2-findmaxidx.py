#최대값 위치 구하기
def find_max_idx(a):
    n = len(a)
    max_idx = 0
    for i in range(1, n):
        if a[max_idx] < a[i]:
            max_idx = i

    return max_idx

a = [1, 5, 4, 2, 3]
print(find_max_idx(a))