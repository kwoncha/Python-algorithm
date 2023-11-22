import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, w):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    q = deque([])
    q.append([x, y, w]) 
    visited[x][y][w] = 1
    while q:
        x, y, w = q.popleft()
        if x == a-1 and y == b-1:
            return visited[x][y][w]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < a and 0 <= ny < b:
                if arr[nx][ny] == 0 and visited[nx][ny][w] == 0:
                    q.append([nx, ny, w])  
                    visited[nx][ny][w] = visited[x][y][w] + 1
                if arr[nx][ny] == 1 and w == 1:
                    q.append([nx, ny, w - 1])  
                    visited[nx][ny][w - 1] = visited[x][y][w] + 1

    return -1

a, b = map(int, input().split())
arr = [[int(i) for i in str(input().strip())] for _ in range(a)]
visited = [[[0] * 2 for _ in range(b)] for _ in range(a)]

result = bfs(0, 0, 1)

print(result)