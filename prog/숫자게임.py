# 1 이진탐색트리 
def solution(A, B):
    answer = 0
    a = sorted(A)
    b = sorted(B)
    
    for i in a:
        left, right = 0, len(b) - 1
        while left <= right:
            mid = (left + right) // 2
            if b[mid] > i:
                right = mid - 1
            else:
                left = mid + 1
        
        if left < len(b):
            answer += 1 
            b.pop(left)  
    
    return answer


# 2 효율성이 제일 좋음
from collections import deque

def solution(A, B):
    answer = 0
    a = deque(sorted(A))
    b = deque(sorted(B))
    
    while b:
        if b[0] > a[0]:
            answer += 1
            b.popleft()
            a.popleft()
        else:
            b.popleft()
    
    return answer

# 3 처음푼 방법 효율성이 제일 안좋음
def count_sort(x, a, b):
    count = 0
    for i in range(len(b)-x):
        if b[i] > a[i+x]:
            count += 1
        else:
            return count
        
    return count

def solution(A, B):
    answer = 0
    a = sorted(A, reverse=True)
    b = sorted(B, reverse=True)
    
    for i in range(len(a)):
        answer = max(answer, count_sort(i, a, b))
        
    return answer