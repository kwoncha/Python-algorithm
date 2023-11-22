# 카카오 출제 문제랑 비슷
# 1번 풀이 bfs로 해결 하려 했지만 실패함
# visited를 설정하지 않은게 문제 풀이의 실패, 내가 설정한 visited는 array임
from collections import deque
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    visited = [[0] * a for _ in range(b)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    co = 0
    for _ in range(c):
        x, y = map(int, input().split())
        visited[x][y] = 1
        d = 0
        q = deque([(x,y,d)])
        
    for i in range(c):
        while q:
            a1, a2, a3 = q.popleft()
            if visited[a1+1][a2] == 1 or visited[a1-1][a2] == 1 or visited[a1][a2-1] == 1 or visited[a1][a2+1] == 1 and 0< d < 2:
                co += 1
                break
            for z in range(4):
                nx = a1 + dx[z]
                ny = a2 + dy[z]
                if 0<= nx < a and 0<= ny < b:
                    if visited[nx][ny] == 1 and d <= 1:
                        q.append((nx, ny, d+1))
                 
    print(co)


# 2번 풀이 이후 dfs로 풀이한 해답을 봄 비슷하지만 bfs보다 간결
# 재귀함수를 이용하여 해결함
import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx, ny)
            
for _ in range(int(input())):
    m, n, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                dfs(i, j)
                result += 1
    print(result)

# 3번 bfs로 다시 해결한 방법
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    visited[x][y] = True
    q = deque([(x, y)])

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if array[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True  
                array[nx][ny] = 0  

    return True

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    array = [[0] * n for _ in range(m)]
    visited = [[False] * n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        array[y][x] = 1  
    result = 0
    for i in range(n):
        for j in range(m):
            if array[j][i] == 1:  
                if bfs(j, i):
                    result += 1

    print(result)