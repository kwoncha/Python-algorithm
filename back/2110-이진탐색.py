# 백준 2110번 이진탐색 문제 
# 처음에 혼자 힘으로 해결하지 못하고 다시 풀어봄 
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) 
answer = [int(input()) for i in range(n)]
answer.sort()

min = 1
max = answer[-1] - answer[0]
result = 0

while min <= max:
    mid = (min + max) // 2
    value = answer[0]
    count = 1
    for i in range(len(answer)):
        if answer[i] >= value + mid:
            value = answer[i]
            count += 1
    if count >= m:
        min = mid + 1
        result = mid
    else:
        max = mid - 1
        
print(result)