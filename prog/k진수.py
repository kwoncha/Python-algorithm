# 1번 단순하게 문제에 소수를 구하지 않고 나와있는 그대로 문제를 품
# k 가 10 일때 정확히 나오지 않음
def solution(n, k):
    answer = 0
    result, asd = [], []
    
    if k < 10:
        while n > 0:
            a = n % k
            n = n // k
            result.append(a)
            
        result = result[-1::-1]
        
    else:
        for i in str(n):
            result.append(int(i))
            
    for i in result:
        b = result.pop()
        if b != 0:
            asd.append(b)
        else:
            asd = []
            answer += 1
            
    if len(asd) != 0:
        answer += 1
        
    return answer

# 2번 
def solution(n, k):
    # k진수로 변환 후 0으로 분할
    result = ''
    while n != 0 :
        result = str(n % k) + result
        n = n//k 
    result =  result.split('0')
# 소수 구하지
    count = 0
    tf = True
    for i in result:
        if i in ('','1'):
            continue

        for j in range(2,int(int(i)**0.5)+1) :
            if int(i) % j == 0 :
                tf = False
                break
        if tf == True : count += 1
    return count