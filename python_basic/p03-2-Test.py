#n명 중 두 명을 뽑아 짝을 짓는다고 할 때 짝을 지을 수 있는 모든 조합을 출력

def nC2(a):
    n = len(a)
    result = list()
    for i in range(n-1):
        for j in range(i+1, n):
            result.append(a[i] + " - " + a[j])
    return result

name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(nC2(name))

