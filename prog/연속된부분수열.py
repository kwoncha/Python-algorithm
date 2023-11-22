# 첫 문제 풀이 시간 복잡도를 통과하지 못함
def solution(sequence, k):
    answer = []
    for i in range(len(sequence)):
        co = 0
        for j in range(i, len(sequence)):
            co += sequence[j]
            if co >= k:
                break
            
        if co == k:
            answer.append([i , i + j])
            
    answer.sort(key=lambda x: x[1] - x[0])
    
    return answer[0]

# 이후 이것을 통해 해결한 방법
def solution(sequence, k):
    answer = []
    n = len(sequence)
    result = [0] * (n + 1)  # 부분합 배열 초기화

    for i in range(1, n + 1):
        result[i] = result[i - 1] + sequence[i - 1]

    min_length = float('inf')
    start, end = 0, 0
    while start < n:
        if result[end] - result[start] == k:
            length = end - start
            if length < min_length:
                min_length = length
                answer = [start, end]
            start += 1
        elif result[end] - result[start] < k:
            end += 1
        else:
            start += 1

        if end > n:
            break

    return [answer[0], answer[1]-1]

# 제일 직관적이고 깔끔하다고 생각하는 사람의 답
def solution(sequence, k):
    start = 0
    end  = 0
    lenS = len(sequence)
    sumS = 0
    resultTemp = []
    while start < lenS or end < lenS:
        if sumS < k and end == lenS:
            break
        if sumS == k: # 같은 경우 해당 인덱스를 저장
            resultTemp.append([start, end - 1])
            sumS -= sequence[start]
            start += 1
        elif sumS < k:
            sumS += sequence[end]
            end += 1
        else:
            sumS -= sequence[start]
            start += 1


    resultTemp.sort(key = lambda x : [x[1] - x[0], x[0]])
    return resultTemp[0]
