# 처음 해결은 시간 복잡도를 통과하지 못함 이것을 heapq를 통해 정렬을 하지 않고 최솟값을 빼는 것으로
# 시간 단축 한것
import heapq

result = []
li = []
count = 0

for _ in range(int(input())):
    a, b = map(int, input().split())
    heapq.heappush(result, (a, b))

while result:
    a, b = heapq.heappop(result)
    
    if len(li) == 0:
        li.append(a)
        li.append(b)
        count += b - a
    else:
        if li[1] >= a:
            count += max(0, b - li[1])
            li[1] = max(li[1], b)
        else:
            li = [a, b]
            count += b - a

print(count)

# 정답지의 답
import sys
input = sys.stdin.readline

n = int(input()) # 선의 개수 N
arr = [] # 모든 선의 정보를 담는 배열
for i in range(n):
    x, y = map(int, input().split())
    arr.append((x, y)) # (시작점, 끝점)

arr.sort() # 시작점을 기준으로 각 선 정렬
result = 0
start, current = arr[0] # 첫 번째 선을 따라 현재 펜을 이동하기
for line in arr: # 하나씩 선들을 확인하며
    x, y = line
    if current >= x: # 현재 펜이 시작점보다 더 크다면
        current = max(current, y) # 최대한 펜을 쭉 긋기
    else: # 현재 펜이 시작점보다 작다면 (새로 그어야 한다면)
        result += current - start
        start = x # 펜을 이용해 새로 선을 긋기 시작한 점
        current = y # 현재 펜의 위치(끝점)
        
result += current - start
print(result)