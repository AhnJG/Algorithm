#하노이의 탑
#입력:  원반 개수 n
#       현재 기둥 from_pos
#       도착 기둥 to_pos
#       보조 기둥 sub_pos
#출력: 원반 옮기는 순서

def hanoi(n, from_pos, to_pos, sub_pos):
    if n==1: #원반이 한개라면 그냥 옮긴다
        print(from_pos, "->", to_pos)
        return

    #n-1개의 원반을 보조기둥으로 이동
    hanoi(n-1, from_pos, sub_pos, to_pos)
    #가장 큰 원반을 목적지로 이동
    print(from_pos, "->", to_pos )
    #보조기둥에 있는 n-1개의 원반을 목적지로 이동
    hanoi(n-1, sub_pos, to_pos, from_pos)

hanoi(3, 1, 3, 2)