# heapq를 사용해서 입력한 숫자 중 0 이 나올때 최소값을 출력하는 문제
import heapq
import sys
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, x)
    
    if x == 0 and len(heap) == 0:
        print(0)
    
    elif x == 0 and len(heap) != 0:
        print(heapq.heappop(heap))