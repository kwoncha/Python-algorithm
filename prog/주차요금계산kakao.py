# 1번 처음 해결한 문제 풀이 요금이 정확히 나오지만 
# out에서의 배열이 맞지 않아 40프로 정답률이 측정됨
def solution(fees, records):
    result, answer, dic, to = [], [], {}, {}
    
    for i in records:
        a, b, c = i.split()
        t, m = a.split(':')
#       처음에 입차 했을경우
        if c == 'IN':
            if b in dic:
                dic[b] = [int(t), int(m)]
            dic[b] = [int(t), int(m)]
            if b not in to:
                to[b] = 0
            
#                 출차 할 때 요금 납부
        else:
            total = int(t) * 60 + int(m) - dic[b][0] * 60 - dic[b][1]
#             dic[b]를 사용하고 지워야함
            dic[b] = 0 
            to[b] += total
            if b not in answer:
                answer.append(b)
                    
    for h in dic.keys():
        if h not in answer:
            answer.append(b)
            
        if dic[h] != 0:
            total = 1439 - dic[h][0] * 60 - dic[h][1]
            to[h] += total
            dic[h] = 0


        if to[h] <= fees[0]:
            dic[h] += fees[1]
    #             dict를 하나 더 생성해서 거기서 요금을 더한 후 최종적으로 answer에 넣을꺼임
        else:
            dic[h] = fees[1] + fees[3] * ((to[h] - fees[0]) // fees[2])
            if (to[h] - fees[0]) % fees[2] != 0:
                dic[h] += fees[3]
    
    for i in answer:
        a = dic[i]
        result.append(a)        
        
    return result


# 비슷하게 해결한 사람의 정답
# try와 except를 사용해서 이것을 담당함 
def solution(fees, records):
    parking = dict()
    stack = dict()

    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute)  # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car]  # 출차 차량 삭제

    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23 * 60 + 59 - minute
        except:
            stack[car] = 23 * 60 + 59 - minute
    a = sorted(stack.items())
    b = []
    c = []
    for i in a:
        b.append(i[1])
    for i in b:
        if i > fees[0]:
            if (i-fees[0]) % fees[2] == 0:
                d = fees[1] + ((i - fees[0]) / fees[2]) * fees[3]
                c.append(int(d))
            else:
                d = fees[1] + (int((i - fees[0]) / fees[2])+1) * fees[3]
                c.append(int(d))
        elif 0 < i <= fees[0]:
            d = fees[1]
            c.append(int(d))
        else: # 0인경우
            c.append(0)
    return c