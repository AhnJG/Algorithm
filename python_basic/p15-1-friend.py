#친구 리스트에서 자신의 모든 친구를 찾는 알고리즘

def print_all_friends(fri_info, start):
    que = []
    done = set()

    que.append(start)
    done.add(start)

    while que:
        p = que.pop(0)
        print(p)

        for x in fri_info[p]:
            if x not in done:
                que.append(x)
                done.add(x)

fri_info = {
    'A' : ['B', 'C', 'D'],
    'B' : ['A', 'C'],
    'C' : ['A', 'B', 'D', 'E'],
    'D' : ['A', 'C'],
    'E' : ['C', 'F'],
    'F' : ['E'],
    'G' : ['H'],
    'H' : ['G']
}

print_all_friends(fri_info, 'A')
print()
print_all_friends(fri_info, 'G')