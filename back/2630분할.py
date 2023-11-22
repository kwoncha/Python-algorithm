import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0]


def di(x, y, N):
    color = arr[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != arr[row][col]:
                di(x, y, N // 2)
                di(x, y + N // 2, N // 2)
                di(x + N // 2, y, N // 2)
                di(x + N // 2, y + N // 2, N // 2)
                return 0
    if color == 0:
        answer[0] += 1
    else:
        answer[1] += 1


di(0, 0, N)
for a in answer:
    print(a)
