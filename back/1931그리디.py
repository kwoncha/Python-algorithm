import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
dp = [0]
count = 0

for s, e in arr:
    if dp[0] <= s:  
        dp[0] = e
        count += 1
        
print(count)
