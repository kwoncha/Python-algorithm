import sys
input = sys.stdin.readline

N = int(input())
A = [*map(int, input().split())]

LIS = [A[0]]
dp = [0] * N
dp[0] = 1

def findPlace(e):
    start = 0
    end = len(LIS) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if LIS[mid] == e:
            return mid
        elif LIS[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

for i in range(1, N):
    if LIS[-1] < A[i]:
        LIS.append(A[i])
        dp[i] = len(LIS)
    else:
        idx = findPlace(A[i])
        LIS[idx] = A[i]
        dp[i] = idx + 1

print(max(dp))
result = []
max_length = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == max_length:
        result.append(A[i])
        max_length -= 1

result.reverse()
print(*result)