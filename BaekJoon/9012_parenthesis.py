#괄호 문자열
n = int(input())
data = []

for _ in range(n):
    data = input()
    stack = []
    res = "YES"
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == ')':
            if len(stack) <= 0:
                res = "NO"
                break
            else:
                stack.pop()
    if len(stack) != 0:
        res = "NO"
    print(res)

