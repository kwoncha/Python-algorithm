# bfs 연습문제, 문제 해결을 하지 못함
from collections import deque

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX

def bfs():
    q = deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
# for 문제 3가지 방향을 넣을 것을 생각하지 못해 풀지 못함
        for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[now_pos] + 1
                q.append(next_pos)
                
print(bfs())