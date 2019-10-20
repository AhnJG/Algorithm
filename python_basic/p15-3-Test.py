#그래프 탐색 문제

def find_graph(a, start):
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        print(p)

        for x in a[p]:
            if x not in done:
                qu.append(x)
                done.add(x)

graph = {
    1:[2, 3],
    2:[4, 5],
    3:[],
    4:[],
    5:[]
}

find_graph(graph, 1)