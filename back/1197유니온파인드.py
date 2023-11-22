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

n = int(input())
graph = [list(map(float, input().split())) for _ in range(n)]
graph.sort(key=lambda x: x[2])
parent = [i for i in range(n+1)]
answer = 0

for s, e, w in graph:
    if find(s) != find(e):
        union(s, e) 
        answer += w

print(answer)
