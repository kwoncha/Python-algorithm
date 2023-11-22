def solution(dirs):
    answer = 0
    result = [0, 0]
    asd = []
    for i in dirs:
        prev = result.copy() # 이동하기 전 좌표 저장
        if i == 'U' and result[1] < 5:
            result[1] += 1
        elif i == 'D' and result[1] > -5:
            result[1] -= 1
        elif i == 'R' and result[0] < 5:
            result[0] += 1
        elif i == 'L' and result[0] > -5:
            result[0] -= 1
        
        # 이동한 좌표가 이전에 지나간 좌표가 아닌 경우
        if prev != result:
            # 현재 좌표와 이전 좌표를 연결하는 경로 저장
            asd.append((tuple(prev), tuple(result)))
            asd.append((tuple(result), tuple(prev))) # 양방향 경로로 저장
            
    # 중복되는 경로 제거
    asd = list(set(asd))
    
    return len(asd) // 2