# 첫 해결 풀이는 dfs를 분리해 재귀함수를 이용
def dfs(x, y, visited):
    global count
    count += array[x][y]
    visited[x][y] = True
    di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in di:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]):
            continue
        if not visited[nx][ny] and array[nx][ny]:
            dfs(nx, ny, visited)

def solution(maps):
    answer = []
    result = []
    array = [[0] * len(i) for i in maps]
    visited = [[False] * len(i) for i in maps]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'X':
                continue
            else:
                array[i][j] = int(maps[i][j])
                result.append([i, j])

    while result:
        count = 0
        x, y = result.pop(0)
        if not visited[x][y]:
            dfs(x, y, visited)
        if count != 0:
            answer.append(count)
            
    if len(answer) == 0:
        answer.append(-1)
        
    return answer

# 두번째는 stack을 사용하여 하나의 def에서 풀이

def solution(maps):
    answer = []
    result = []
    array = [[0] * len(i) for i in maps]
    visited = [[False] * len(i) for i in maps]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'X':
                continue
            else:
                array[i][j] = int(maps[i][j])
                result.append([i, j])

    while result:
        count = 0
        x, y = result.pop(0)
        if not visited[x][y]:
            stack = [[x, y]]
            while stack:
                ax, ay = stack.pop()
                if not visited[ax][ay]:
                    count += array[ax][ay]
                    visited[ax][ay] = True
                    di = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for dx, dy in di:
                        nx, ny = ax + dx, ay + dy
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and array[nx][ny]:
                            stack.append([nx, ny])

        if count != 0:
            answer.append(count)

    if len(answer) == 0:
        answer.append(-1)

    return sorted(answer)