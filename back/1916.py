import heapq

n= int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visi = [1e19] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

start, end = map(int, input().split())
def di(start):
    q = []
    heapq.heappush(q, (0, start))
    visi[start] = 0
    while q:
        di, now = heapq.heappop(q)
        if visi[now] < di: continue
        for i in arr[now]:
            cost = di + i[1]
            if cost < visi[i[0]]:
                visi[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
di(start)
print(visi[end])