n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [0]* (m+1)
dp[0] = 1

for i in arr:
    for j in range(i, m+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
print(dp[m])