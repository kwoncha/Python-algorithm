# 처음 푼 문제 해결법은 l까지 도달하는 거리와 e까지 도달하는 거리를 찾아서 더하는 것
# 정답에 도출하지 못함
from collections import deque

def solution(maps):
    answer, co = 0, 0
    count = 0
    q = deque([[0,0]])
    arr = [[False] * len(maps) for _ in range(len(maps))]
    while q:
        x, y = q.popleft()
        if not arr[x][y]:
            arr[x][y] = True
            if maps[x][y] == 'L':
                co = 1
                break

            for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                nx, ny = dx+ x, dy+ y
                if 0 <= nx <len(maps) -1 and 0 <= ny < len(maps) - 1 and maps[nx][ny] != 'X' and not arr[nx][ny]:
                    count += 1
                    q.append([nx, ny])
                    
    arr = [[False] * len(maps) for _ in range(len(maps))]
    q = deque([[x, y]])
    while q:
        x, y = q.popleft()
        if not arr[x][y]:
            arr[x][y] = True
            if maps[x][y] == 'E':
                return count
            
            for dx, dy in [(1,0), (-1,0), (0,1), (0, -1)]:
                nx, ny = dx+ x, dy+ y
                if 0 <= nx < len(maps) -1 and 0 <= ny < len(maps) - 1 and maps[nx][ny] != 'X' and not arr[nx][ny]:
                    count += 1
                    print(nx, ny)
                    q.append([nx, ny])
                
    return -1

# 두개의 좌표를 지정해서 합치는 방법
from collections import deque

def solution(maps):
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    def bfs(r, c):
        Q = deque()
        Q.append((r,c))
        while Q:
            x, y = Q.popleft()
            for _ in range(4):
                nx, ny = x + dx[_], y + dy[_]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
                    continue
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1 
                    Q.append((nx, ny))
                    
    a, b, c, d = -1, -1, -1, -1
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S': 
                a, b = i, j
            if maps[i][j] == 'E': 
                c, d = i, j
            if maps[i][j] == 'L':
                visited[i][j] = 0
                bfs(i, j)
    if visited[a][b] == -1 or visited[c][d] == -1:
        return -1
    return visited[a][b] + visited[c][d]