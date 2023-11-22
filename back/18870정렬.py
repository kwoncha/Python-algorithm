# 처음에 for문 2개를 돌리거나 while문을 돌려 시간 초과
n = int(input())
array = list(map(int, input().split()))
l = len(array)
result = [0] * l

for i in range(l):
    array[i] = (array[i], i)
    
array.sort()
co = set()
# set을 통해 동일 한 것 삭제
for i in range(l):
    a, b = array[i]
    if a not in co:
        # 들어 있지 않다면 앞에까지가 정렬된 숫자여서 바로 result에 추가
        result[b] = len(co)
        # 이후 set에 넣어 다음 정렬된 것을 생각
        co.add(a)
        
        # 만약 동일하다면 co의 숫자를 1줄여서 넣으면됨
    else:
        result[b] = len(co) - 1
    
for i in result:
    print(i, end=' ')