# 1715번 문제 그리디와 힙을 이용하여 문제 품

import heapq
heap = []
for i in range(int(input())):
    x = int(input())
    heapq.heappush(heap, x)
    
result = 0

while len(heap) != 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    c = a + b
    result += c
    heapq.heappush(heap, c)
    
print(result)