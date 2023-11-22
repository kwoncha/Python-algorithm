def solution(keyinput, board):
    answer = [0,0]
    x=(board[0]-1)/2
    y=(board[1]-1)/2

    for i in keyinput:
        if i =="up":
            if y >= answer[1]+1:
                answer[1] += 1
            else:
                continue
        elif i =="down":
            if -y <= answer[1]-1:
                answer[1] -= 1
            else:
                continue
        elif i =="right":
            if x >= answer[0]+1:
                answer[0] += 1
            else:
                continue
        elif i=="left":
            if -x <= answer[0]-1:
                answer[0] -= 1
            else:
                continue
    return answer