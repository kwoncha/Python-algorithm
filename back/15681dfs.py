import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000) 
n, m, k=map(int,sys.stdin.readline().split(' '))

arr = [[] for _ in range(n+1)]
visit = [-1] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(now):
    global visit
    visit[now] = 1
    for i in arr[now]:
        if visit[i] == -1:
            visit[now] += dfs(i)
    return visit[now]

dfs(m)
for _ in range(k):
    x = int(input())
    print(visit[x])
