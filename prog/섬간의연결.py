# 1
def solution(n, costs):
    answer = 0
    uni = [0] * (n + 1)
    costs.sort(key = lambda x: x[2])
    for i in range(1,n + 1):
        uni[i] = i
    def union(x,y):
        a = find(x)
        b = find(y)
        if a != b:
            uni[a] = b
    def find(x):
        if uni[x] == x: return x
        else:
            uni[x] = find(uni[x])
            return uni[x]
    for n1,n2,cost in costs:
        if find(n1) != find(n2):
            union(n1,n2)
            answer += cost
    return answer

# 2
import heapq

def solution(n, costs):
    answer = 0
    arr = [[-1 for _ in range(n)] for _ in range(n)]
    for i in costs:
        a, b, c = i
        arr[a][b] = c
        arr[b][a] = c

    q = []
    heapq.heappush(q, (0, 0))
    visited = {}
    while q:
        dist, now = heapq.heappop(q)
        if now not in visited:
            visited[now] = True
            answer += dist
            for g in range(n):
                if arr[now][g] != -1:
                    heapq.heappush(q, (arr[now][g], g))
                    
    return answer