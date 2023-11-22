def solution(topping):

    dic = {}
    set_dic = set()
    res = 0

    for i in topping:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in topping:
        dic[i] -= 1
        set_dic.add(i)

        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            res += 1

    return res