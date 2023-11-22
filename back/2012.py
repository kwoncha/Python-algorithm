# 그리디 알고리즘 
n= int(input())
result = []
ans = 0

for i in range(n):
    m = int(input())
    result.append(m)
       
result.sort()

for i in range(1, n+1):
    ans += abs(i- result[i-1])
print(ans)