def solution(s):
    answer = 0
    length = len(s)
    
    for i in range(length):
        count = 1  
        start, end = i, i
        
        while start > 0 and end < length - 1 and s[start - 1] == s[end + 1]:
            count += 2
            start -= 1
            end += 1
        
        answer = max(answer, count)
        
        count = 0  
        start, end = i, i + 1
        

        while start >= 0 and end < length and s[start] == s[end]:
            count += 2
            start -= 1
            end += 1
        
        answer = max(answer, count)
    
    return answer