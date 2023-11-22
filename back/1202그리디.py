# 처음에 해결한 답
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
re, ba = [], []
for i in range(n):
    a, b = map(int, input().split())
    re.append((a,b))
for _ in range(m):
    ba.append(int(input()))
    
ba.sort()
re.sort(key=lambda x: (x[1],-x[0]), reverse=True)
visited = [0] * n
q = []
for i in range(n):
    # 이부분에서 반례가 존재해서 안됨 다음에 다시 시작할 때는 밑에서 부터 다시 시작해야함
    while q and q[-1][0] <= ba[0]:
        c = q.pop()
        ba.pop(0)
        answer += c[1]
    q.append(re[i])
print(answer)


# 이후 다른 사람의 풀이
import sys
input = sys.stdin.readline
import heapq 

n, k = map(int, input().split())
stones = []
for i in range(n):
    weight, price = map(int, input().split())
    stones.append((weight, price))
    
bags = []
for i in range(k):
    bag = int(input())
    bags.append(bag)
    
stones.sort()
bags.sort()
heap = [] 
cur = 0
result = 0
# 여기까지 동일하고 heapq를 통해 시간복잡도를 줄임
for bag in bags: 
    while cur < n:
        weight, price = stones[cur]
        if bag >= weight:
            heapq.heappush(heap, -price)
            cur += 1
        else:
            break
    if len(heap) > 0:
        price = -heapq.heappop(heap)
        result += price
        
print(result)