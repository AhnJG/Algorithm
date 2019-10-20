# #2557
# print('Hello World!')
#
# #7287
# print(9)
# print('arki13')
#
# #10172
# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')
#
# #10718
# print('강한친구 대한육군\n'*2)
#
# #11718
# while True:
#     try:
#         print(input())
#     except EOFError:
#         break
#
# #10869
# a, b = map(int, input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# #10430
# a, b, c = map(int, input().split())
# print((a + b) % c)
# print((a % c + b % c) % c)
# print((a * b) % c)
# print((a % c * b % c) % c)

# #2741 N 찍기
# for i in range(1, (int)(input()) + 1):
#     print(i)

# #2742 기찍 N
# N = (int)(input())
# for i in range(N):
#     print(N-i)

#2739 구구단
# n = (int)(input())
# for i in range(1, 10):
#     print(n, '*', i, '=', n*i)

#2438 별 찍기 - 1
# n = (int)(input())
# for i in range(1, n+1):
#     print('*'*i)

#2439 별 찍기 - 2
# a=int(input())
# for i in range(1,a+1):
#     print(" "*(a-i) + "*"*i)

#2440 별 찍기 - 3
# n = int(input())
# for i in range(n+1):print('*'*(n-i))

#2441 별 찍기 - 4
# n = int(input())
# for i in range(n+1):
#     print(' '*i + '*'*(n-i))

#1924 2007년
# N = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# m, d = map(int, input().split())
# sum_d = d-1
# for i in range(m-1):
#     sum_d += N[i]
#
# print(Week[sum_d % 7])

#8393 합
# sum = 0
# for i in range(1, int(input())+1):
#     sum += i
# print(sum)

#11720 숫자의 합
# N = int(input())
# # n = int(input())
# # sum = 0
# # for i in range(N):
# #     sum += n % 10
# #     n = n//10
# # print(sum)

#2839 설탕 배달
# tmp = n = int(input())
# i = j = cnt = 0
# cnt_res = 2000
# while n - i > 0:
#     tmp = tmp - (5 * i)
#     cnt = cnt + i
#     i = i + 1
#     while tmp >= 3:
#         tmp = tmp - 3
#         cnt = cnt + 1
#     if tmp != 0:
#         cnt = -1
#     if cnt < cnt_res and cnt != -1:
#         cnt_res = cnt
#     cnt = 0
#     tmp = n
#
# if cnt_res != 2000:
#     print(cnt_res)
# else:
#     print('-1')

#11721 열 개씩 끊어 출력하기
# str = input()
# for i in range(len(str)):
#     import sys
#     sys.stdout.write(str[i])
#     if (i + 1) % 10 == 0:
#         print()

#15552 빠른 A + b
# import sys
# n = int(sys.stdin.readline())
# for i in range(n):
#     a = sys.stdin.readline()
#     a1, b1 = a.split(' ')
#     print(int(a1) + int(b1))

#9498 시험 성적
# n = int(input())
# if n >=90:
#     print('A')
# elif n >= 80:
#     print('B')
# elif n >= 70:
#     print('C')
# elif n >= 60:
#     print('D')
# else:
#     print('F')

#10817 세 수
# a = input().split(' ')
# a = [int(i) for i in a]
# a.sort()
# print(a[1])

#10871 X보다 작은 수
# n, x = map(int, input().split())
# list = input().split(' ')
# for i in range(n):
#     if int(list[i]) < x:
#         import sys
#         sys.stdout.write(list[i] + ' ')

#1546 평균
# n = int(input())
# score = input().split()
# score = [int(i) for i in score]
# score.sort()
# sum = 0
# for i in range(len(score)):
#     score[i] = score[i] / score[-1] * 100
#     sum += score[i]
# print('%f' % (sum / len(score)))

#4344 평균은 넘겠지
# for i in range(int(input())):
#     N, *sco = map(int, input().split())
#     avg = sum(sco) / N
#     print('%.3f%%'%(sum([1 for j in sco if j > avg]) / N * 100))
    #print('%d'%(sum([1 for j in sco if j > avg])))
    #print('{0:.3f}%'.format(len(cnt)/N*100))

#1110 더하기 사이클
# res = num = int(input())
# cnt = 0
# while True:
#     add1 = res // 10
#     add2 = res % 10
#     res = (add1+add2)%10 + (add2*10)
#     cnt += 1
#     if res == num:
#         break
# print(cnt)

#4673 셀프 넘버
# for i in range(1, 10000):
#     tmp = i
#     check = False
#     arr = []
#     for j in range(1, 36):
#         while True:
#             arr.append((tmp - 1) % 10)
#             tmp = tmp // 10
#
#             if tmp is 0:
#                 sum = sum(arr)

#10872 팩토리얼
# n = int(input())
# sum1 = 1
# for i in range(1, n+1):
#     if n is 0:
#         break
#     sum1 *= i
# print(sum1)

#10952 A+B - 5
# while True:
#     a, b = map(int, input().split())
#     if a is 0 and b is 0:
#         break
#     print(a+b)

#1476 날짜 계산
# e, s, m = map(int, input().split())
# i = 0
# while True:
#     e_ = i % 15 + 1
#     s_ = i % 28 + 1
#     m_ = i % 19 + 1
#     i += 1
#     if e is e_ and s is s_ and m is m_:
#         print(i)
#         break

#11654 아스키 코드
# print(ord(input()))

#10809 알파뱃 찾기
# arr = [-1 for i in range(26)]
# s = input()
# for i in range(len(s)):
#     if arr[ord(s[i]) - 97] is -1:
#         arr[ord(s[i]) - 97] = i
#
# for i in range(26):
#     print(arr[i], end = ' ')

#2675 문자열 반복
# n = int(input())
# for i in range(n):
#     cnt, s = input().split(' ')
#     for j in range(len(s)):
#         print(s[j]*int(cnt), end = '')
#     print()

#11365 !밀비 급일
# while True:
#     s = input()
#     if s == 'END':
#         break
#     for i in range(1, len(s)+1):
#         print(s[len(s)-i], end = '')
#     print()

#2902 KMP는 왜 KMP일까?
# s = input().split('-')
# for _ in s:
#     print(_[0], end = '')

#2941 크로아티아 알파벳
# s = input()
# cnt = 0
# pos = 0
# while pos < len(s):
#     if s[pos:].find('c=') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('c-') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('dz=') is 0:
#         cnt += 1
#         pos += 3
#     elif s[pos:].find('d-') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('lj') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('nj') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('s=') is 0:
#         cnt += 1
#         pos += 2
#     elif s[pos:].find('z=') is 0:
#         cnt += 1
#         pos += 2
#     else:
#         cnt += 1
#         pos += 1
# print(cnt)

#2941 크로아티아 알파벳 - 2
# s = input()
# dics = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# for dic in dics:
#     s = s.replace(dic, "_")
# print(len(s))

#1065 한수
# n = int(input())
# cnt = 0
# for i in range(1, n+1):
#     arr = []
#     while i is not 0:
#         arr.append(i%10)
#         i = i // 10
#
#     if len(arr) is 1:
#         cnt += 1
#         continue
#     else:
#         gap = arr[1] - arr[0]
#         check = True
#
#     for j in range(1, len(arr)):
#         if gap == arr[j] - arr[j-1]:
#             gap = arr[j] - arr[j-1]
#         else:
#             check = False
#             break
#     if check:
#         cnt += 1
# print(cnt)

#1085 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# min = 1001
# if min > (x - 0):
#     min = x - 0
# if min > (w - x):
#     min = w - x
# if min > (y - 0):
#     min = y - 0
# if min > (h - y):
#     min = h - y
# print(min)

#1085 직사각형에서 탈출 - 2
# x, y, w, h = map(int, input().split())
# print(min(x, y, w-x, h-y))

#1237 정ㅋ벅ㅋ
#print('문제의 정답')

#2556 별 찍기 - 14 X
# n = int(input())
# for i in range(n):
#     print('*' * 5)

#2750 수 정렬하기
# import sys
# n = int(input())
# list_ = []
# for i in range(n):
#     list_.append(int(sys.stdin.readline()))
# list_ = list(set(list_))
# list_.sort()
# for i in range(len(list_)):
#     sys.stdout.write(str(list_[i])+ '\n')

#10944 랜덤 게임~~
# import random
# print(int(random.random() * 10000 + 1))

#10951 A + B - 4
# while True:
#     try:
#         a, b = map(int, input().split())
#         print(a+b)
#     except EOFError:
#         break

#10953 A + B - 6
# for i in range(int(input())):
#     a, b = map(int, (input().split(',')))
#     print(a+b)

#11021 A + B - 7
# for i in range(int(input())):
#     a, b = map(int, (input().split(' ')))
#     print('Case #%d: %d + %d ='%((i+1), a, b), a+b)

#15740 A + B - 9 X
# s1, s2 = input().split(' ')
# s3 = list()
# upper = 0
# i = 1
# while True:
#     if i > max(len(s1), len(s2)):
#         if upper:
#             s3.append(upper)
#         break
#     print(int(s1[-i]), int(s2[-i]))
#     if int(s1[-i]) and int(s2[-i]):
#          s3.append((upper + int(s1[-i]) + int(s2[-i])) % 10)
#          upper = (upper + int(s1[-i]) + int(s2[-i])) // 10
#     elif int(s1[-i]):
#         s3.append((upper + int(s1[-i])) % 10)
#         upper = (upper + int(s1[-i])) // 10
#     elif int(s2[-i]):
#         s3.append((upper + int(s2[-i])) % 10)
#         upper = (upper + int(s2[-i])) // 10
#     i += 1
#
#
# for i in range(1, len(s3)+1):
#     import sys
#     sys.stdout.write(str(s3[len(s3) - i]))

#print(s3)

#1978 소수 찾기
# n = int(input())
# num = map(int, input().split(' '))
# cnt = 0
# for nu in num:
#     loop = 2
#     cnt += 1
#     while True:
#         if nu is 1: cnt -= 1; break
#         if loop >= nu:break
#         if nu % loop is 0:
#             cnt -= 1
#             break
#         loop += 1
# print(cnt)

#9653 스타워즈 로고
# print('    8888888888  888    88888')
# print('   88     88   88 88   88  88')
# print('    8888  88  88   88  88888')
# print('       88 88 888888888 88   88')
# print('88888888  88 88     88 88    888888')
# print('')
# print('88  88  88   888    88888    888888')
# print('88  88  88  88 88   88  88  88')
# print('88 8888 88 88   88  88888    8888')
# print(' 888  888 888888888 88  88      88')
# print('  88  88  88     88 88   88888888')

#5337 웰컴
# print('.  .   .')
# print('|  | _ | _. _ ._ _  _')
# print('|/\\|(/.|(_.(_)[ | )(/.')

#9654 나부 함대 데이터
# print('SHIP NAME      CLASS          DEPLOYMENT IN SERVICE')
# print('N2 Bomber      Heavy Fighter  Limited    21        ')
# print('J-Type 327     Light Combat   Unlimited  1         ')
# print('NX Cruiser     Medium Fighter Limited    18        ')
# print('N1 Starfighter Medium Fighter Unlimited  25        ')
# print('Royal Cruiser  Light Combat   Limited    4         ')

#10171 고양이
# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

#10170 NFC West vs North
# print('NFC West       W   L  T')
# print('-----------------------')
# print('Seattle        13  3  0')
# print('San Francisco  12  4  0')
# print('Arizona        10  6  0')
# print('St. Louis      7   9  0')
# print('')
# print('NFC North      W   L  T')
# print('-----------------------')
# print('Green Bay      8   7  1')
# print('Chicago        8   8  0')
# print('Detroit        7   9  0')
# print('Minnesota      5  10  1')

#2108 통계학
# import sys
# num = int(sys.stdin.readline())
# List = []
# for i in range(num):
#     List.append(int(sys.stdin.readline()))
#
# # 산술평균
# print('%.0f'%(sum(List)/len(List)))
#
# List.sort()
# #중앙값
# print(List[len(List)//2])
#
# from collections import Counter
# #데이터가 등장한 횟수 구하기 , 사전 형식으로
# c = Counter(List)
# #최빈값 구하기 ★★★
# order = c.most_common()
# #order.sort()
# maximum = order[0][1]
# modes = []
# for num in order:
#     if num[1] == maximum:
#         modes.append(num[0])
# if len(modes) is 1: print(modes[0])
# else: print(modes[1])
#
# #범위
# print(max(List)-min(List))

#5338 마이크로소프트 로고
# print('       _.-;;-._')
# print('\'-..-\'|   ||   |')
# print('\'-..-\'|_.-;;-._|')
# print('\'-..-\'|   ||   |')
# print('\'-..-\'|_.-\'\'-._|')

#5339 콜센터
# print('     /~\\')
# print('    ( oo|')
# print('    _\\=/_')
# print('   /  _  \\')
# print('  //|/.\\|\\\\ ')
# print(' ||  \\ /  ||')
# print('============')
# print('|          |')
# print('|          |')
# print('|          |')

#2442 별찍기 5
# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1), end='')
#     print('*' * (i * 2 + 1))

#2443 별 찍기 6
# num = int(input())
# for i in range(num):
#     print(' ' * i, end='')
#     print('*' * (num * 2 - i * 2 - 1))

#2444 별 찍기 7
# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1), end='')
#     print('*' * (i * 2 + 1))
# for i in range(1, num):
#     print(' ' * i, end='')
#     print('*' * (num * 2 - i * 2 - 1))

#2445 별 찍기 8
# num = int(input())
# for i in range(num):
#     print('*' * (i + 1), end='')
#     print(' ' * (num * 2 - (i + 1) * 2), end='')
#     print('*' * (i + 1))
# for i in range(1, num):
#     print('*' * (num - i), end='')
#     print(' ' * (i * 2), end='')
#     print('*' * (num - i))

#2446 별 찍기 9
# num = int(input())
# for i in range(num):
#     print(' ' * i, end='')
#     print('*' * (num * 2 - i * 2 - 1))
# for i in range(1, num):
#     print(' ' * (num - i - 1), end='')
#     print('*' * (i * 2 + 1))

#2552 별 찍기 12
# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1), end='')
#     print('*' * (i + 1))
# for i in range(1, num):
#     print(' ' * (i), end='')
#     print('*' * (num - i))

#별 찍기 13
# num = int(input())
# for i in range(num):
#     print('*' * (i + 1))
# for i in range(1, num):
#     print('*' * (num - i))

#별 찍기 14
# num = int(input())
# for i in range(num):
#     print('*' * num)

#10990 별 찍기 15
# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1), end='')
#     print('*', end='')
#     print(' ' * (2*i - 1), end='')
#     print('*' * bool(i))

#10991 별 찍기 16
# num = int(input())
# for i in range(num):
#     print(' ' * (num - i - 1), end='')
#     print('* ' * (i + 1))

#10992 별 찍기 17
# num = int(input())
# for i in range(num-1):
#     print(' ' * (num - i - 1), end='')
#     print('*', end='')
#     print(' ' * (2*i - 1), end='')
#     print('*' * bool(i))
# print('*' * (num * 2 - 1))

#10995 별 찍기 20
# num = int(input())
# for i in range(num):
#     print(' ' * bool(i%2), end='')
#     print('* ' * num)

#10996 별 찍기 21
# num = int(input())
# for i in range(num):
#     print('* ' * ((num + 1) // 2))
#     print(' *' * (num // 2))

#13015 별 찍기 23
# n = int(input())
# print('*' * n, end='')
# print(' ' * (2 * (n - 1) - 1), end='')
# print('*' * n)
# for i in range(1, n):
#     print(' ' * i, end='')
#     print('*', end='')
#     print(' ' * (n - 2), end='')
#     print('*', end='')
#     print(' ' * (2 * (n - (1 + i)) - 1), end='')
#     print('*' * bool((i + 1) % n), end='')
#     print(' ' * (n - 2), end='')
#     print('*')
# for i in range(2, n):
#     print(' ' * (n - i), end='')
#     print('*', end='')
#     print(' ' * (n - 2), end='')
#     print('*', end='')
#     print(' ' * (2 * (i - 2) + 1), end='')
#     print('*', end='')
#     print(' ' * (n - 2), end='')
#     print('*')
# print('*' * n, end='')
# print(' ' * (2 * (n - 1) - 1), end='')
# print('*' * n)

#2577 숫자의 개수
# n = []
# for i in range(3):
#     n.append(int(input()))
# m = str(n[0] * n[1] * n[2])
# for i in range(10):
#     print(m.count(str(i)))

#8958 OX퀴즈
# n = int(input())
# for i in range(n):
#     m = input()
#     sum = 0
#     adder = 0
#     for j in m:
#         if j is 'O':
#             adder += 1
#         else:
#             adder = 0
#         sum += adder
#     print(sum)

#10039 평균 점수
# n = []
# for i in range(5):
#     n.append(int(input()))
#     if n[i] < 40 : n[i] = 40
# print(sum(n) // 5)

#2920 음계
# n = input().split(' ')
# m = n[0]
# for c in n[1:]:
#     m += c
# if m == '12345678' : print('ascending')
# elif m == '87654321' : print('descending')
# else : print('mixed')

#1152 단어의 개수
# import sys
# n = sys.stdin.readline().split(' ')
# cnt = 0
# for i in range(len(n)):
#     i -= cnt
#     if n[i] is '' or n[i] is '\n':
#         del n[i];
#         cnt +=1;
# sys.stdout.write(str(len(n)))

#1157 단어 공부
# n = input()
# from collections import Counter
# m = Counter(n.upper())
# l = m.most_common()
# if len(l) > 1 and l[0][1] == l[1][1] : print('?')
# else : print(l[0][0])

#5622 다이얼
# n = input()
# sum = 0
# for ch in n:
#     if ch < 'D' : sum += 3
#     elif ch < 'G' : sum += 4
#     elif ch < 'J' : sum += 5
#     elif ch < 'M' : sum += 6
#     elif ch < 'P' : sum += 7
#     elif ch < 'T' : sum += 8
#     elif ch < 'W' : sum += 9
#     else : sum += 10
# print(sum)

#2908 상수
# n = input().split(' ')
# n[0] = list(n[0])
# n[1] = list(n[1])
# n[0][0], n[0][2] = n[0][2], n[0][0]
# n[1][0], n[1][2] = n[1][2], n[1][0]
# # n[0] = str(n[0])
# # n[1] = str(n[1])
# big = max(n[0], n[1])
# res = ""
# for ch in big:
#     res += ch
# print(res)

#1316 BASE32 디코딩
# n = input()
# import base64
# res = base64.b32decode(n, casefold=True)
# print(res.decode('utf-8'))

#15963 CASIO
# a, b = map(int, input().split(' '))
# if a - b : print('0')
# else : print('1')

#15936 이상한 기호
# a, b = map(int, input().split(' '))
# print((a + b) * (a - b))

#15965 K번째 소수
# n = int(input())
# def is_prime(n: int) -> bool:
#     if n < 2 : return False
#     if n in (2, 3, 5, 7) : return True
#     if (n % 2 is 0) or (n % 3 is 0) or (n % 5 is 0) or (n % 7 is 0): return False
#     k, _ = 11, round(n ** 0.5) + 1
#     while k <= _ :
#         if (n % k is 0) or (n % (k + 2) is 0): return False
#         k += 6
#     return True
# cnt = 0
# num = 1
# while cnt != n:
#     num += 1
#     if is_prime(num):
#         cnt += 1
# print(num)

#n = int(input())
# def is_prime(n: int) -> int:
#     seive = [False, False] + [True] * (n - 1)
#     print(seive)
#     seive[4::2] = [False] * ((n - 2) // 2)
#     seive[6::3] = [False] * ((n - 3) // 3)
#     seive[10::5] = [False] * ((n - 5) // 5)
#     seive[14::7] = [False] * ((n - 7) // 7)
#     for k in range(2, n+1):
#         if seive[k]:
#             seive[k*2::k] = [False] * ((n + 1 - k) // k)
#         return [x for x in range(n+1) if seive[x]]
# res = is_prime(1000)
# # print(res[50])
# print(res)

#1929 소수 구하기
# a, b = map(int, input().split())
# def is_prime(n: int) -> bool:
#     if n < 2 : return False
#     if n in (2, 3, 5, 7) : return True
#     if (n % 2 is 0) or (n % 3 is 0) or (n % 5 is 0) or (n % 7 is 0): return False
#     k, _ = 11, round(n ** 0.5) + 1
#     while k <= _ :
#         if (n % k is 0) or (n % (k + 2) is 0): return False
#         k += 6
#     return True
#
# while a <= b:
#     if is_prime(a):
#         print(a)
#     a += 1

#2581 소수
# a = int(input())
# b = int(input())
# def is_prime(n: int) -> bool:
#     if n < 2 : return False
#     if n in (2, 3, 5, 7) : return True
#     if (n % 2 is 0) or (n % 3 is 0) or (n % 5 is 0) or (n % 7 is 0): return False
#     k, _ = 11, round(n ** 0.5) + 1
#     while k <= _ :
#         if (n % k is 0) or (n % (k + 2) is 0): return False
#         k += 6
#     return True
#
# pri = []
# while a <= b:
#     if is_prime(a):
#         pri.append(a)
#     a += 1
# if pri :
#     print(sum(pri))
#     print(pri[0])
# else :
#     print('-1')

#15965 소수 성공!!
# table = [True for i in range(10000001)]
# table[0], table[1] = False, False
#
# def eratos():
#     for i in range(2, 100001):
#         if table[i]:
#             for j in range(i*2, 10000001, i):
#                 table[j] = False
#
# cnt = 0
# eratos()
# n = int(input())
# k = 0
# while cnt < n:
#     k += 1
#     if table[k]:
#         cnt += 1
# print(k)

#15966 군계일학 X
# n = int(input())
# prog = []
# for i in range(n):
#     prog.append(int(input()))
# cnt = 1
# for k in prog[1:]:
#     if k is (prog[0] + cnt):
#         cnt += 1
# print(cnt)

#14645 와이버스 부릉부릉
# a, b = map(int, input().split(' '))
# for i in range(a):
#     n = input()
# print('비와이')
