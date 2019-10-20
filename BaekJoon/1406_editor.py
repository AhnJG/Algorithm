# #에디터
# #연결리스트
#
# import sys
# data = sys.stdin.readline().rstrip()
# n = int(sys.stdin.readline())
# point = len(data)
#
# for _ in range(n):
#     order = sys.stdin.readline().rstrip()
#     if len(order) > 1: #P일때
#         d1 = data[:point]
#         d2 = data[point:]
#         data = d1 + order[2] + d2
#         point += 1
#     elif order == 'L':
#         if point == 0:
#             continue
#         else:
#             point -= 1
#     elif order == 'D':
#         if point == len(data):
#             continue
#         else:
#             point += 1
#     elif order == 'B':
#         if point == 0:
#             continue
#         else:
#             d1 = data[:point-1]
#             d2 = data[point:]
#             data = d1 + d2
#             point -= 1
# sys.stdout.write(data)

# leftST = list(input())
# rightST = []
# N = int(input())
# for i in range(N):
#     cmd = input().split()
#     if cmd[0] == 'L':
#         if not leftST:
#             continue
#         ch = leftST.pop()
#         rightST.append(ch)
#     elif cmd[0] == 'D':
#         if not rightST:
#             continue
#         ch = rightST.pop()
#         leftST.append(ch)
#     elif cmd[0] == 'B':
#         if not leftST:
#             continue
#         leftST.pop()
#     elif cmd[0] == 'P':
#         leftST.append(cmd[1])
# while leftST:
#     ch = leftST.pop()
#     rightST.append(ch)
# output = ''
# while rightST:
#     output += rightST.pop()
# print(output)