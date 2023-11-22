# dfs와 bfs, 재귀를 사용해서 문제 해결하려고 함
# 첫 문제 해결은 짧은 시간 복잡도를 가졌지만 일부 문제에서 시간 초과를 나타냄
from collections import deque

def solution(x, y, n):
    visited = [0] * 100001
    result = deque([[x, 0]])
    
    while result:
        a, b = result.popleft()
        
        if a == y:
            break
        
        if a < y:
            result.append([a + n, b + 1])
            result.append([2 * a, b + 1])
            result.append([3 * a, b + 1])
    
    if a != y:
        b = -1
    
    return b

# 이후 방문의 수를 정해두고 방문수가 다를 경우 다시 방문 하도록 만드니 시간복잡도를 통과함
from collections import deque

def solution(x, y, n):
    visited = [0] * 1000001
    result = deque()
    result.append((x, 0))
    visited[x] = 1
    
    while result:
        a, b = result.popleft()
        
        if a == y:
            return b
        
        for na in (a + n, a * 2, a * 3):
            if na <= y and not visited[na]:
                visited[na] = 1
                result.append((na, b+1))
    
    return -1
