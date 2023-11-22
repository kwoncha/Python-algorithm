import sys
input = sys.stdin.readline
import heapq

def di():
    q = []
    heapq.heappush(q, (0, 1))
    visit[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if visit[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < visit[i[0]]:
                visit[i[0]] = cost
                co[i[0]].append((i[0], i[1]))
                heapq.heappush(q, (cost, i[0]))

n, m, k = map(int, input().split())
arr = [[] for _ in range(n+1)]
co = [[] for _ in range(n+1)]
visit = [1e9] * (n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
# 카운트를 해서 k보다 커지면 안됨    
count = 0 
di()
print(visit[n-1])
