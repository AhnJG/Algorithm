# method 1
# n = int(input())

# for i in range(n):
#     print(n-i)

# method 2
n = int(input())
print("\n".join(map(str, range(n, 0, -1))))