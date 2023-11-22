import sys
input = sys.stdin.readline
import heapq

def di():
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if result[start][now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < result[start][i[0]]:
                result[start][i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
n, m = map(int, input().split())
arr= [[] for i in range(n + 1)]
result = [[1e18] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

for i in range(1, n+1):
    start = i
    di()

answer = 1e18
for i in range(1, n+1):
    if result[i][i] != 1e18:
        answer = min(answer, result[i][i])

if answer != 1e18:
    print(answer)
else:
    print(-1)