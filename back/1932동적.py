n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [[0]*(n) for _ in range(n)]
result[0][0] = arr[0][0]
for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        if j - 1 >= 0:
            result[i][j] = max(result[i-1][j] + arr[i][j] , result[i-1][j-1] + arr[i][j])
        else:
            result[i][j] = result[i-1][j] + arr[i][j]
print(max(result[n-1]))