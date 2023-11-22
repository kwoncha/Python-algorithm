import sys
from collections import deque
input = sys.stdin.readline
# 1
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        curr = q.popleft()
        for next in graph[curr]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

n = int(input())
m = int(input())
g = [list(map(int,input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            graph[i].append(j)
visited = [False for _ in range(n)]
plan = list(map(int, input().split()))
bfs(plan[0]-1)
answer = True
for i in plan:
    if not visited[i-1]:
        answer = False
        break 
if answer:
    print("YES")
else:
    print("nO")


# 2
n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
parents = list(range(n))
plan = list(map(int, input().split()))


def find(a):
    if a == parents[a]:
        return a
    else:
        return find(parents[a])


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union(i, j)

ans = "YES"
for i in range(1, m):
    if parents[plan[i] - 1] != parents[plan[0] - 1]:
        ans = "NO"
        break

print(ans)