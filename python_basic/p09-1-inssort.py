#Insertion Sort
#O(n^2)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        print(a)
    return a

a = [5, 4, 2, 3, 1]
print(ins_sort(a))
