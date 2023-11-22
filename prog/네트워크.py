#1 dfs
def dfs(node, visit, computers):
    visit[node] = True
    for i in range(len(computers[node])):
        if not visit[i] and computers[node][i] == 1:
            dfs(i, visit, computers)

def solution(n, computers):
    visit = [False] * len(computers)
    count = 0

    for i in range(n):
        if not visit[i]:
            dfs(i, visit, computers)
            count += 1

    return count



# 2 유니온 파인드
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x != y:
        parent[y] = x

def solution(n, computers):
    parent = [i for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                union(parent, i, j)

    answer = set()
    for i in range(n):
        answer.add(find(parent, i))

    return len(answer)