# 주어진 2차원 리스트에서 성적 평균값 등수를 리스트 순서에 맞게 추출하기
def solution(score):
    answer = []
    for i in score:
        answer.append(i[0]+i[1])
    result = sorted(answer, reverse = True)
    return [result.index(i)+1 for i in answer]