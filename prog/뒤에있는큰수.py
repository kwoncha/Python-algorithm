# 1번 해결은 시간 초과로 실패, 이것 말고 이중 for문 사용도 시간 초과로 실패
def solution(numbers):
    answer = []
            
    for i in range(len(numbers)-1):
        j = i + 1
        while j < len(numbers):
            if numbers[j] > numbers[i]:
                answer.append(numbers[j])
                break
                
            else:
                j += 1
        
        if (i + 1) != len(answer):
            answer.append(-1)
            
    answer.append(-1)
    
    return answer

# 이후 스텍을 사용하여 문제를 해결
def solution(numbers):
    answer = [-1]*(len(numbers))
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer