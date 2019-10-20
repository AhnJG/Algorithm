#Selection Sort
#시간 복잡도 O(n^2)

def sel_sort(a):
    n = len(a)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if a[min_idx] > a[j]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

a = [1, 4, 2, 3, 5]
print(sel_sort(a))

