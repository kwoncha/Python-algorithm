#  동적 계획법 문제 처음에는 다른 방식으로 해결했지만 50%만 맞춤
def solution(n, money):
    answer = 0
    a = set(money)
    result = [i for i in a]
    result.sort()
    for i in range(len(result)):
        m = n
        co = n // result[i]
        if n % result[i] == 0:
            answer += 1
            while co > 0:
                co -= 1
                m -= result[i]
                for j in range(i + 1, len(result)):
                    if m != 0 and m % result[j] == 0:
                        answer += 1
                
    return answer % 1000000007


def solution(n, money):
    answer = 0
    money_set = set(money)
    result = sorted(list(money_set))
    count = [0] * (n + 1)
    count[0] = 1

    for coin in result:
        for i in range(coin, n + 1):
            count[i] += count[i - coin]

    answer = count[n] % 1000000007

    return answer
