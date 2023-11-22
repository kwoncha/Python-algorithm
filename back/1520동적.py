import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    count = 0
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if arr[nx][ny] < arr[x][y]:
            count += dfs(nx, ny)

    dp[x][y] = count
    return count

result = dfs(0, 0)
print(result)