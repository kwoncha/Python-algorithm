import heapq

n = int(input())
result, heap = [], []
# 문제들을 heapq에 넣어 데드라인으로 정렬
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(heap, (a, b))

while heap:
    x, y = heapq.heappop(heap)
    c = x
    heapq.heappush(result, y)
    # 데드라인 초과하면 원소 제거
    if c < len(result):
        heapq.heappop(result)
        
print(sum(result))

# 처음에는 데드라인을 생각하지 못해 틀렸음
n = int(input())
result = {}
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    if a not in result:
        result[a] = b
        
    else:
        if result[a] < b:
            result[a] = b
            
print(sum(result.values()))