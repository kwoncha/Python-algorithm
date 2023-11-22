import sys
from collections import deque
input = sys.stdin.readline

a, b, c = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(b)] for _ in range(c)]
q = deque()

for h in range(c):
    for i in range(b):
        for j in range(a):
            if arr[h][i][j] == 1:
                q.append([i, j, h])

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
while q:
    x, y, z = q.popleft()
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < b and 0 <= ny < a and 0 <= nz < c:
            if arr[nz][nx][ny] == 0:
                arr[nz][nx][ny] = arr[z][x][y] + 1
                q.append([nx, ny, nz])

ans = 0
for h in arr:
    for line in h:
        for tomato in line:
            if tomato == 0:
                print(-1)
                exit()
            ans = max(ans, tomato)

print(ans - 1)