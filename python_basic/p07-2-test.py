#Linear Search_순차 탐색, 선형 탐색, 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘
#리스트 a, 찾는 값 x
#계산 복잡도 O(n)
def search_list(a, x):
    n = len(a)
    result = list()
    for i in range(n):
        if a[i] == x:
            result.append(i)

    return result

a = [1, 4, 2, 3, 1, 7, 1, 6, 9]
print(search_list(a, 1))
print(search_list(a, 0))
