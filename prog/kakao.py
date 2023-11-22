# 19년도 카카오 인턴십 문제
def solution(board, moves):
    result = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                result.append(board[j][i-1])
                board[j][i-1] = 0


                if len(result) > 1:
                    if result[-1] == result[-2]:
                        result.pop(-1)
                        result.pop(-1)
                        answer += 2     
                break

            
    return answer