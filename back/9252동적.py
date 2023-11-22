import sys
input = sys.stdin.readline

x = list(input().strip())
y = list(input().strip())
a = [[0, ''] for _ in range(len(y) + 1)] 

for i in range(1, len(x) + 1):
    b = a.copy() 
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            b[j] = [a[j - 1][0] + 1, a[j - 1][1] + x[i - 1]]
        else:
            if b[j - 1][0] > a[j][0]: 
                b[j] = [b[j - 1][0], b[j - 1][1]]
            else:
                b[j] = [a[j][0], a[j][1]]
    a = b

for i in a[len(y)]:
    print(i)