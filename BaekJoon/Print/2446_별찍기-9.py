# method 1
# n = int(input())

# for i in range(n):
#     print(' '*i + '*'*(2*(n-i)-1))

# for i in range(1, n):
#     print(' '*(n-i-1) + '*'*(2*(i+1)-1))

# method 2
n = int(input())
for i in range(-n+1, n): 
    print(' '*(n-abs(i)-1) + '*'*(2*abs(i)+1))