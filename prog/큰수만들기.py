# 탐욕 알고리즘 활용
def solution(number, k):
    result = []
    for i in number:
        while result and result[-1] < i and k > 0:
# result가 비어있지 않고 result의 마지막 숫자가 현재 숫자 i보다 작고 제거할 k가 남아 있을때
            k -= 1
            result.pop()
# 다돌아가면 result 제거
        result.append(i)
    if k != 0:
        result = result[:-k]
# 다돌렸는데 앞에가 크면 k가 0이 되지 않을때 뒤에를 제거
    return ''.join(result)