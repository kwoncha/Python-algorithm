# 1 bfs로 해결하니 효율성에서 다 실패함 시간 초과
from collections import deque

def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    for i in range(len(puddles)):
        x, y = puddles[i]
        arr[y-1][x-1] = -1
        
    def bfs(start):
        q = deque([start])
        mi = 1e9
        co = 0
        while q:
            x, y, count = q.popleft()
            if x == m - 1 and y == n - 1:
                if mi > count:
                    mi = count
                    co = 1
                elif mi == count:
                    co += 1
                    
            for dx, dy in ((1, 0), (0, 1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if arr[ny][nx] == 0 or arr[ny][nx] >= count + 1:
                    arr[ny][nx] = count + 1
                    q.append((nx, ny, count + 1))
        return co
    answer = bfs((0, 0, 0))
    return answer % 1000000007

# 2 동적
def solution(m, n, puddles):
    dp = [[0]*m for _ in range(n)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(m):
            if [j+1,i+1] in puddles:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1] % 1000000007