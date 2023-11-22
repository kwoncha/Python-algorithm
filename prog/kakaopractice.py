def solution(today, terms, privacies):
    result = []
    today = list(map(int, today.split('.')))
    today = today[2] + today[1] * 28 + today[0] * 28 * 12

    dic = dict()
    for term in terms:
        k, v = term.split()
        dic[k] = int(v) * 28

    for i in range(len(privacies)):
        datetime, category = privacies[i].split()
        datetime = list(map(int, datetime.split('.')))
        datetime = datetime[2] + datetime[1] * 28 + datetime[0] * 28 * 12
        if datetime + dic[category] <= today:
            result.append(i+1)

    return result

def solution(id_list, report, k):
    answer = []
    return answer