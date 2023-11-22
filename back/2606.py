# dfs를 사용한 문제 풀이
def dfs(v):
    visited[v] = True
    # 한번 돌 때 마다 노드를 측정
    a[0].append(1)
    for e in a[v]:
        if not(visited[e]):
            dfs(e)
            
n = int(input())
m = int(input())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
    
for e in a:
    e.sort()

visited = [False] * (n+1)
dfs(1)
# 1이 걸린 것도 포함되기 때문에 1을 뺌
print(len(a[0]) - 1)


# 다른 사람 답안 global을 알지 못해 저렇게 사용하지 않고 다른 리스트에 추가함
n = int(input())
m = int(input())
adj = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)

def dfs(now_pos):
    global count
    count += 1
    visited[now_pos] = True
    for next_pos in adj[now_pos]:
        if not visited[next_pos]:
            dfs(next_pos)
dfs(1)
print(count - 1)