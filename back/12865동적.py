# 동적 프로그래밍 기초
n, m = map(int, input().split())
a = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    b, c = map(int, input().split())
    for j in range(1, m+1):
        if j < b:
            a[i][j] = a[i - 1][j]
        else:
            a[i][j] = max(a[i-1][j], a[i-1][j-b] + c)
            
print(a[n][m])