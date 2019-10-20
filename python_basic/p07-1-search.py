#Linear Search_순차 탐색, 선형 탐색
#리스트 a, 찾는 값 x
def search_list(a, x):
    n = len(a)
    for i in range(n):
        if a[i] == x:
            return i

    return -1

a = [1, 4, 2, 3, 5, 7, 8, 6, 9]
print(search_list(a, 4))
print(search_list(a, 0))
