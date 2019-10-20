#Merge Sort
#O(nlogn)

def mer_sort(a):
    n = len(a)
    if n <= 1:
        return

    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    mer_sort(g1)
    mer_sort(g2)

    i = 0
    while g1 and g2:
        if g1[0] > g2[0]:
            a[i] = g2.pop(0)
        else:
            a[i] = g1.pop(0)
        i += 1

    while g1:
        a[i] = g1.pop(0)
        i += 1

    while g2:
        a[i] = g2.pop(0)
        i += 1

a = [5, 3, 2, 4, 1]
mer_sort(a)
print(a)

