n=int(input())
k=int(input())
 
s,e = 1,n*n
while s <= e:
    value = (s+e)//2
    idx = sum(min(value//i,n) for i in range(1,n+1))
    if idx >= k:
        result = value
        e = value - 1
    else:
        s = value + 1
        
print(result)