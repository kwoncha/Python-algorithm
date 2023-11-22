import sys
input = sys.stdin.readline
import heapq

def di():
    q = []
    heapq.heappush(q, (0, start))
    result[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if result[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < result[i[0]]:
                result[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
                
n, m = map(int, input().split())
start = int(input())
arr= [[] for i in range(n + 1)]
result = [1e9] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    

di()
for i in range (1, n + 1):
    if result[i] == 1e9:
        print("INF")
    else:
        print(result[i])