import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    else:
        return find(parent[a])

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

while True:
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(m)]
    graph.sort(key=lambda x: x[2])
    parent = [i for i in range(n+1)]
    answer = 0

    for s, e, w in graph:
        if find(s) != find(e):
            union(s, e)

        else:
            answer += w

    print(answer)