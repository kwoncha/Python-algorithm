import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1

answer = abs(arr[start] + arr[end])
result = [arr[start], arr[end]]

while start < end:
    current = arr[start] + arr[end]
    if abs(current) < answer:
        answer = abs(current)
        result = [arr[start], arr[end]]
        if answer == 0:
            break

    if current < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])