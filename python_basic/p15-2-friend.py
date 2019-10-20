#친구 리스트에서 자신의 모든 친구들의 친밀도 계산

def print_all_friends(fri_info, start):
    que = []
    done = set()

    que.append((start, 0))
    done.add(start)

    while que:
        p, d = que.pop(0)
        print(p, d)

        for x in fri_info[p]:
            if x not in done:
                que.append((x, d+1))
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