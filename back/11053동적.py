# 동적 프로그래밍, 가장 긴 증가하는 부분 수열
n = int(input())
result = [1] * n
answer = list(map(int, input().split()))

for i in range(1, n):
    for j in range(i):
        if answer[j] < answer[i]:
            result[i] = max(result[i], result[j] + 1)

print(max(result))