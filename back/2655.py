# 코드를 작성 했지만 답을 도출하지 못함
import sys
input = sys.stdin.readline

n = int(input())
answer, result, co = [], [[0] * (n+1) for _ in range(n+1)], [[] for _ in range(n+1)]

for i in range(n):
    answer.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, len(answer)):
        if answer[j-1][0] > answer[j][0] and answer[j-1][2] > answer[j][2]:
            result[i][j] += answer[j-1][1]
            co[i].append(j)
        else:
            result[i][j] = max(result[i-1][j], answer[j][1] + result[i-1][j-1])
            if answer[j][1] + result[i-1][j-1] > result[i-1][j]:
                co[i].append(j)

print(len(co[n]))
for h in range(len(co[n])-1, -1, -1):
    print(co[n][h])

# 이후  본 해결책 처음 리스트에 입력 번호를 같이 삽입함
# 높이를 중심으로 최대 값을 도출하고 그에 따른 번호를 출력

n = int(input())
array = []
array.append((0, 0, 0, 0))
for i in range(1, n + 1):
    area, height, weight = map(int, input().split())
    array.append((i, area, height, weight))

# 무게를 기준으로 정렬
array.sort(key=lambda data: data[3])
dp = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(0, i):
        if array[i][1] > array[j][1]:
            dp[i] = max(dp[i], dp[j] + array[i][2])

max_value = max(dp)
index = n
result = []
while index != 0:
    if max_value == dp[index]:
        result.append(array[index][0])
        max_value -= array[index][2]
    index -= 1
    
result.reverse()
print(len(result))
[print(i) for i in result]