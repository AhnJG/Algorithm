#동명이인 찾아 집합으로 되돌려주기
def find_same_name(a):
    n = len(a)
    result = set()
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                result.add(a[i])
    return result

name =  ["Tom", "Jerry", "Mike", "Tom"]
print(find_same_name(name))
name2 =  ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))