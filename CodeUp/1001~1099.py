#1012 : [기초-입출력] 실수 한 개 입력받아 그대로 출력하기
# n = float(input())
# print("%f" % n)

#1013 : [기초-입출력] 정수 두 개 입력받아 그대로 출력하기
# n1, n2 = map(int, input().split())
# print(n1, n2)

#1014 : [기초-입출력] 문자 두 개 입력받아 순서 바꿔 출력하기
# a, b = input().split()
# print(b, a)

#1015 : [기초-입출력] 실수 한 개 입력받아 소수점 이하 둘째 자리까지 출력하기
# n = float(input())
# print('%.2f' % n)

#1017 : [기초-입출력] 정수 한 개 입력받아 세 번 출력하기
# n = int(input())
# for i in range(3):
#     print(n, end=' ')

#1018 : [기초-입출력] 시간 입력받아 그대로 출력하기
# h, m = map(int, input().split(':'))
# print("%d:%d"%(h, m))

#1019 : [기초-입출력] 년월일 입력받아 형식에 맞게 출력하기
# y, m, d = map(int, input().split('.'))
# print('%04d.%02d.%02d'%(y, m, d))

#1020 : [기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
# f, b = map(int, input().split('-'))
# print("%06d%07d"%(f, b))

#1021 : [기초-입출력] 단어 한 개 입력받아 그대로 출력하기
#1022 : [기초-입출력] 문장 한 개 입력받아 그대로 출력하기
# w = input()
# print(w)

#1023 : [기초-입출력] 실수 한 개 입력받아 부분별로 출력하기
# n1, n2 = map(int, input().split('.'))
# print(n1)
# print(n2)

#1024 : [기초-입출력] 단어 한 개 입력받아 나누어 출력하기
# s = input()
# for ch in s:
#     print('\'%c\''%ch)

#1025 : [기초-입출력] 정수 한 개 입력받아 나누어 출력하기
# s = input()
# tmp = 10000
# for ch in s:
#     print("[%d]"%(int(ch)*tmp))
#     tmp /= 10

#1026 : [기초-입출력] 시분초 입력받아 분 만 출력하기
# h, m, s = map(int, input().split(':'))
# print(m)

# 1027 : [기초-입출력] 년월일 입력받아 형태 바꿔 출력하기
# y, m, d = map(int, input().split('.'))
# print("%02d-%02d-%04d"%(d, m, y))

# 1028 : [기초-데이터형] 정수 한 개 입력받아 그대로 출력하기2
# n = int(input())
# print(n)

# 1029 : [기초-데이터형] 실수 한 개 입력받아 그대로 출력하기2
# d = float(input())
# print("%.11f"%d)

# 1030 : [기초-데이터형] 정수 한 개 입력받아 그대로 출력하기3
# n = int(input())
# print(n)

# 1031 : [기초-출력변환] 10진수 한 개 입력받아 8진수로 출력하기
# n = int(input())
# print("%o"%n)

# 1032 : [기초-출력변환] 10진 정수 한 개 입력받아 16진수로 출력하기1
# n = int(input())
# print("%x"%n)

# 1033 : [기초-출력변환] 10진 정수 한 개 입력받아 16진수로 출력하기2
# n = int(input())
# print("%X"%n)

# 1034 : [기초-출력변환] 8진 정수 한 개 입력받아 10진수로 출력하기
# n = int(input(), 8)
# print(n)