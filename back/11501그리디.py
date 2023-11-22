import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input()) 
    arr = list(map(int, input().split())) 
    a = arr[n - 1] 
    tar = [0] * n 
    for i in range(n - 1, -1, -1):
        a = max(a, arr[i])
        tar[i] = a
    result = 0
    for i in range(n):
        result += max(0, tar[i] - arr[i])
    print(result)