import sys
input = sys.stdin.readline

n = input().strip()
m = int(input())
dic = {}
d = 0
for i in range(m):
    a, b, c = input().split()
    b, c = int(b), int(c)
    if d != a:
        d = a
        count = 0
        for j in range(len(n)):
            if n[j] == a:
                count += 1
            dic[j] = count
    if n[b] != a:        
        print(dic[c] - dic[b])
    else:
        print(dic[c] - dic[b] + 1)