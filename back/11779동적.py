import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

count = [-1] * (n + 1)
distance = [1e9] *(n + 1)
x, y = map(int, input().split())

def di(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if distance[now] < dis:
            continue
        for i in arr[now]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                count[i[0]] = now
                heapq.heappush(q,(cost, i[0]))


def path(y):
    a = [y]
    pa = y
    while y != x:
        pa = count[y]
        a.append(pa)
        y = pa 
    return a[::-1]

di(x)
print(distance[y])
print(len(path(y)))
print(*path(y))
