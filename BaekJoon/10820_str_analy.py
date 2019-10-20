#문자열 분석
import sys

while True:
    try:
        data = input()
        low = 0
        up = 0
        n = 0
        space = 0
        for x in data:
            if x >= 'A' and x <= 'Z':
                up += 1
            elif x >= 'a' and x <= 'z':
                low += 1
            elif x >= '0' and x <= '9':
                n += 1
            elif x == ' ':
                space += 1
        sys.stdout.write(str(low) + ' ' + str(up) + ' ' + str(n) + ' ' + str(space) + '\n')
    except EOFError:
        break
