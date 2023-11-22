from collections import deque

n = int(input())
arr = []
count = []
visited = [[False] * n for _ in range(n)] 
for i in range(n):
    a = list(str(input()))
    arr.append(a)
    
for i in range(n):
    for j in range(n):
        co = 0
        if arr[i][j] == '1' and not visited[i][j]:
            q = deque([(i,j)])
            while q:
                x, y = q.popleft()
                if not visited[x][y]:
                    co += 1
                    visited[x][y] = True
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny] == '1':
                            q.append((nx, ny))
                        
            count.append(co)
     
count.sort()            
print(len(count))

for i in count:
    print(i)