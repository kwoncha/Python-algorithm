# 처음 해결한 방법, 짝꿍이 중복되는건 안되는 줄 알았음 하지만 인원수만 빠지면 중복 가능
def solution(weights):
    co = 0
    dic = {}
    weights.sort()
    a = []
    for i in weights:
        if i not in dic:
            dic[i] = 1
            a.append(i)
            
        else:
            dic[i] += 1
                    
    for i in range(len(a)-1):
        if dic[a[i]] > 1:
            co += 1
            
        for j in range(i+1, len(a)):    
            if a[i] * 3 == a[j] * 2 or a[i] * 4  == a[j] * 3 or a[i] * 4 == a[j] * 2:
                co += 1
                
    if dic[a[-1]] > 1:
        co += 1
                
    return co
    
# 이후 풀이
def solution(weights):
    answer = 0
    dic = {}

    for w in weights:
        if w in dic:
            dic[w] += 1
        else:
            dic[w] = 1

    for i in dic:
        if dic[i] > 1:
            answer += (dic[i] * (dic[i] - 1)) / 2
        if i * 2 in dic:
            answer += dic[i] * dic[i * 2]
        if i * 2 / 3 in dic:
            answer += dic[i] * dic[i * 2 / 3]
        if i * 3 / 4 in dic:
            answer += dic[i] * dic[i * 3 / 4]

    return answer