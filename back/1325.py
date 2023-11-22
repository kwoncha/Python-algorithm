# 1번 풀이 dfs를 사용한 풀이 예제는 통과하지만 정답은 x
def dfs(i):
    co[i].append(1)
    visited[i] = True
    for j in adj[i]:
        if not visited[j]:
            dfs(j)
            
n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
co = [[b] for b in range(n+1)]


for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)
    
for i in range(1, n+1):
    visited = [False] * (n + 1)
    dfs(i)
    
co.sort(key=lambda x: len(x))

for e in range(1, len(co)):
    a = len(co[1])
    if len(co[e]) == a:
        print(co[e][0], end=' ')
    
    else:
        break

# 2번 bfs로 풀이한 정답
from collections import deque

n, m = map(int, input().split())
adj = [[] for _ in range(n +1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[y].append(x)

def bfs(v):
    q = deque([v])
    visited = [False] * (n +1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in adj[v]:
            if not visited[e]:
                q.append(e)
                visited[e] = True
                count +=1
    return count

result = []
max_value = -1

for i in range(1, n +1):
    c = bfs(i)
    if c > max_value:
        result = [i]
        max_value = c
    elif c == max_value:
        result.append(i)
        max_value = c

for e in result:
    print(e, end=" ")