#Binary Search
#시간복잡도 O(log2(n))

def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return -1


a = [i**2 for i in range(1, 10)] #[1, 4, 9, 16, 25, 36, 49, 64, 81]

print(binary_search(a, 16))
print(binary_search(a, 24))
