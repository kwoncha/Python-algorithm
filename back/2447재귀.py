def kan(n):
    if n == 1:
        return ['*']
    start = kan(n//3)
    arr = []
    for s in start:
        arr.append(s*3)
    for s in start:
        arr.append(s+' '*(n//3)+s)
    for s in start:
        arr.append(s*3)
    return arr

n = int(input())
print('\n'.join(kan(n)))