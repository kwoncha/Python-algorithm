import sys 
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])  


def union(a, b):
    a = find(a)
    b = find(b)

    if a != b: # 랭크 설정해서 깊이를 통해 최적화 만드는 작업
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
parent = list(range(n+1))
rank = [0] * (n+1)
results = []

for i in arr:
    a, b, c = i
    if a == 0:
        union(b, c)
    else:
        if find(b) == find(c):
            results.append('YES')
        else:
            results.append('NO')

for i in results:
    print(i)