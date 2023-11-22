# 처음 풀이 방향
# 리스트에 최대 값과 최소값을 넣어 수정 변환하여 최댓값을 구하는 방식으로 품
# 예제 한 문제는 통과하지만 예상과 다르게 나머지는 해결되지 않음
a, b, c = map(int, input().split())
list1 = [[b, c] for _ in range(a+1)]
list2 = list(map(int, input().split()))
list2.append(0)

for i in range(1, a+1):
    if list1[i-1][0] - list2[i-1] >= 0:
        list1[i][0] = list1[i-1][0] - list2[i-1]
        if list1[i-1][1] + list2[i-1] > c:
            list1[i][1] = list1[i-1][1] - list2[i-1]
            
        else:
            list1[i][1] = list1[i-1][1] + list2[i-1]
            
    else:
        list1[i][0] = list1[i-1][0] + list2[i-1]
        if list1[i-1][1] + list2[i-1] > c:
            list1[i][1] = list1[i-1][1] - list2[i-1]

        else:
            list1[i][1] = list1[i-1][1] +list2[i-1]
            
if 0 <= max(list1[a]) and max(list1[a]) <= c:
    print(max(list1[a]))
    
else:
    if 0 <= min(list1[a]) and min(list1[a]) <= c:
        print(min(list1[a]))
    else:
        print(-1)
        

# 2번 방법은 동적 과정을 통해 해결
# 동적과정을 통해 코드의 효율성과 간결성을 높힘
n, s, m = map(int, input().split())
array = list(map(int, input().split()))
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if dp[i - 1][j] == 0:
            continue
        if j - array[i - 1] >= 0:
            dp[i][j - array[i - 1]] = 1
        if j + array[i - 1] <= m:
            dp[i][j + array[i - 1]] = 1

result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
        
print(result)