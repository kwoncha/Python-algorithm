import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input()) 
arr2 = list(map(int, input().split()))

dp = [[0]*(30*500+1) for _ in range(n+1)] 

result = set()

def di(arr1, m, now, left, right):
    new = abs(left- right)

    if new not in result:
        result.add(new)
    if now == n:
        return 0
    if dp[now][new] == 0:
        di(arr1, m, now+1, left + arr1[now], right)
        di(arr1, m, now+1, left , right+ arr1[now])
        di(arr1, m, now+1, left, right)
        dp[now][new] = 1

di(arr1, m, 0, 0, 0)
answer = []

for i in arr2:
    if i in result:
        answer.append("Y")
    else:
        answer.append("N")

print(*answer)