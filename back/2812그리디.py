# 처음에 푼 알고리즘, 제일 작은 값부터 제거하면 큰 값이 나올 거라 생각 하지만 반례가 존재
n, m = map(int, input().split())
arr1 = int(input())
arr2 = str(arr1)
result, co = [], {}
answer = ''
for i in range(len(arr2)):
    a = arr1 % 10
    arr1 = arr1 // 10
    result.append(a)
    
result.sort()
for i in range(m):
    b = result.pop(0)
    if b not in co:
        co[b] = 1
    else:
        co[b] += 1

for i in range(len(arr2)):
    if int(arr2[i]) in co:
        co[int(arr2[i])] -= 1
        if co[int(arr2[i])] == 0:
            co.pop(int(arr2[i]))
    
    else:
        answer += arr2[i]
                
print(int(answer))

# 2번째 풀이, 왼쪽부터 큰수가 나오면 stack에 넣고 작은 것들은 뺌
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = input().strip() 
deleted = 0 
stack = [] 

for x in data:
    while len(stack) > 0 and stack[-1] < x:
        if deleted == k:
            break
            
        else:
            stack.pop()
            deleted += 1
    stack.append(x)
# 이후 만약 다 안빠졋다면 작은값부터 제거
for i in range(k - deleted):
    stack.pop()
    
print(''.join(stack))