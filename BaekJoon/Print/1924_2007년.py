k = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30] #0~11월
l = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

m, d = map(int, input().split())

print(l[(sum(k[0:m])+d-1) % 7])