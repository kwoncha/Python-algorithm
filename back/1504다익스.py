import sys
input = sys.stdin.readline
import heapq

def di():
    q = []
    heapq.heappush(q, (0, start))
    result[start][start] = 0
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
result = [[1e9] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))

no1, no2 = map(int, input().split())
for i in [1, no1, no2, n]:
    if len(arr[i]) != 0:   
        start = i
        di()

answer = min(result[1][no1] + result[no1][no2] + result[no2][n], result[1][no2] + result[no2][no1] + result[no1][n])
if any(i == 1e9 for i in (result[1][no1], result[no1][no2], result[no2][n], result[1][no2], result[no2][no1], result[no1][n])):
    print(-1)
else:
    print(answer)
