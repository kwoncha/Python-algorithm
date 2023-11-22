n = int(input())
result = []
for i in range(n):
    m = int(input())
    a, b = 0, 0
    arr = list(map(int, input().split()))
    arr.sort()
    c = arr[-1] - arr[-2]
    for i in range(0, m - 2):
        if i % 2 == 0:
            a = max(a, arr[i+2] - arr[i])
        else:
            b = max(b, arr[i+2] - arr[i])
    print(max(a, b, c))    