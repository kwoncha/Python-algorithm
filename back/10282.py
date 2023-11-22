from collections import deque
# 처음 해결한 풀이 하지만 오류가 생김
def bfs(v):
    q = deque([v])
    visited = [False] * (n + 1)
    visited[v[0]] = True
    count = 1
    co = 0
    while q:
        r, w = q.popleft()
        for e in ad[r]:
            if not visited[e[0]]:
                q.append((e[0], 0))
                visited[e[0]] = True
                count += 1
                co += e[1]

    return count, co

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    ad = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, s = map(int, input().split())
        ad[b].append((a, s))

    x, y = bfs((k,0))
    for u in [x, y]:
        print(u, end=' ')

# 정답으로 채택된 답안
# bfs로만 풀려고 했던 방식과 다르게 heapq를 사용해 최단 거리를 이용하여 문제 해결
# 최단거리를 출력하는 것을 빼먹어서 틀림
import heapq
import sys
input = sys.stdin.readline
def dijkstra(start):
    heap_data = []
    heapq.heappush(heap_data, (0, start))
    distance[start] = 0
    while heap_data:
        dist, now = heapq.heappop(heap_data)
        if distance[now] < dist: 
            continue
        for i in adj[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap_data, (cost, i[0]))
                
for _ in range(int(input())):
    n, m, start = map(int, input().split())
    adj = [[] for i in range(n + 1)]
    distance = [1e9] * (n + 1)
    for _ in range(m):
        x, y, cost = map(int, input().split())
        adj[y].append((x, cost))
    dijkstra(start)
    count = 0
    max_distance = 0
    for i in distance:
        if i != 1e9:
            count += 1
            if i > max_distance:
                max_distance = i
                
    print(count, max_distance)