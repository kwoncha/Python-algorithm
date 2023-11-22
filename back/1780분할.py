import sys
input = sys.stdin.readline

N = int(input())
PAPER = [list(map(int, input().split())) for _ in range(N)]
answer = [0, 0, 0]


def traversal(x, y, N):
    color = PAPER[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != PAPER[row][col]:
                traversal(x, y, N // 3)
                traversal(x, y + N // 3, N // 3)
                traversal(x, y + 2 * (N // 3), N // 3)
                traversal(x + N // 3, y + 2 * (N // 3), N // 3)
                traversal(x + N // 3, y, N // 3)
                traversal(x + 2 * (N // 3), y + N // 3, N // 3)
                traversal(x + 2 * (N // 3), y , N // 3)
                traversal(x + N // 3, y + N // 3, N // 3)
                traversal(x + 2 * (N // 3), y + 2 * (N // 3), N // 3)
                return 0
    if color == -1:
        answer[0] += 1
    elif color == 0:
        answer[1] += 1
    else:
        answer[2] += 1


traversal(0, 0, N)
for a in answer:
    print(a)
