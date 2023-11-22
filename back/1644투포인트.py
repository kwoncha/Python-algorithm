import sys
input = sys.stdin.readline

n = int(input())

def sieve(n):
    array = [True] * (n + 1)
    array[0] = array[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            for j in range(i * i, n + 1, i):
                array[j] = False
    return [i for i in range(n + 1) if array[i]]

if n > 1:
    arr = sieve(n)
else:
    print(0)
    exit()

start = 0
end = start
answer, result = 0, 0

while start < len(arr):
    if answer >= n:
        if answer == n:
            result += 1
        answer -= arr[start]
        start += 1
        

    elif end == len(arr):
        break

    else:
        answer += arr[end]
        end += 1

print(result)