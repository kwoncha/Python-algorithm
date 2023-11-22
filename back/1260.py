# 첫 풀이 틀림
from collections import deque

def BFS(graph, root):
    v = []
    queue = deque([root])
    
    while queue:
        n = queue.popleft()
        if n not in v:
            v.append(n)
            if n in v:
                t = list(set(graph[n])-set(v))
                t.sort()
                queue += t
            
    return ''.join(str(i) for i in v)

# DFS
def DFS(graph, root):
    v= []
    s= [root]
    
    while s:
        n = s.pop()
        if n not in v:
            v.append(n)
            if n in graph:
                t = list(set(graph[n])-set(v))
                t.sort(reverse=True)
                s += t
            
    return ''.join(str(i) for i in v)

graph = {}
a,b,c = map(int, input().split())

for _ in range(b):
    n1, n2 = map(int, input().split())
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)
        
    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)
        
print(DFS(graph, c))
print(BFS(graph, c))

# 2번째 다른 사람의 답 코드가 더 간결하고 dfs를 재귀 함수를 통해 표현
from collections import deque
def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in adj[v]:
        if not(visited[e]):
            dfs(e)
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=' ')
            for e in adj[v]:
                if not visited[e]:
                    q.append(e)
                    
n, m, v = map(int, input().split())
adj = [[] for _ in range(n +1)]
# 전체의 리스트를 담아야해서 n+1개의 리스트가 있어야함
for _ in range(m): 
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
for e in adj:
    e.sort()

visited = [False] * (n +1)
dfs(v)
print()
visited = [False] * (n +1)
bfs(v)