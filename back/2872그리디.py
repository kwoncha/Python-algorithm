n = int(input())
a, b = [], []
answer = 0
for _ in range(n):
    m = int(input())
    a.append(m)
    b.append(m)
a.sort(reverse=True)
co = 0
for i in range(len(a)-1, -1, -1):
    if a[co] == b[i]:
        answer += 1
        co += 1
        
print(len(b) - answer)