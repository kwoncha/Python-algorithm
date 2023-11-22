def solution(storey):
    answer = 0
    result = []
    st = str(storey)
    for i in range(len(st)):
        result.append(int(st[i]))

    while result:
        cn = result.pop()
        if cn < 5:
            answer += cn
        elif cn == 5:
            answer += 5
            if len(result) > 0 and result[-1] >= 5:
                result[-1] += 1
        else:
            answer += 10 - cn
            if len(result) > 0:
                result[-1] += 1
            else:
                answer += 1

    return answer