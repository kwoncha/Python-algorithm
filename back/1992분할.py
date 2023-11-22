import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().strip())) for _ in range(N)] 

def di(x, y, N):
    color = arr[x][y]
    for row in range(x, x + N):
        for col in range(y, y + N):
            if color != arr[row][col]:
                upper_left = di(x, y, N // 2)
                upper_right = di(x, y + N // 2, N // 2)
                lower_left = di(x + N // 2, y, N // 2)
                lower_right = di(x + N // 2, y + N // 2, N // 2)
                return '(' + upper_left + upper_right + lower_left + lower_right + ')'
    return color  

answer = di(0, 0, N)
print(answer)