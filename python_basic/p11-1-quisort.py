#Quick Sort
#평균O(nlogn), 최악O(n^2)

def qui_sort(a, start, end):
    if end - start <= 0:
        return

    pivot = a[end]
    i = start

    for j in range(start, end):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[end] = a[end], a[i]

    qui_sort(a, start, i-1)
    qui_sort(a, i+1, end)


a = [1, 4, 2, 5, 3]
qui_sort(a, 0, len(a)-1)
print(a)