n = int(input())
stack = []
for _ in range(n):
    order= input()
    if ' ' in order:
        order, data = order.split(' ')

    if order == "push":
        stack.append(data)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])