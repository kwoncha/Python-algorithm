# 처음으로 해결한 방법
def solution(skill, skill_trees):
    answer = 0
    co = 0
    for i in skill_trees:
        for j in i:
            if j in skill:
                if j == skill[co]:
                    co += 1
                else:
                    break
            
            else:
                continue
                
        co = 0
        if j == i[-1]:
            answer += 1
    
    return answer


# 수정을 통해 정제된 방법
def solution(skill, skill_trees):
    answer = 0
    
    for skills in skill_trees:
        result = [s for s in skills if s in skill]
        
        if "".join(result) == skill[:len(result)]:
            answer += 1

    return answer