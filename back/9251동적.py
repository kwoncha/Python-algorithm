# 1번 처음에 문제 푼 방식 최대 공통 수열이 아닌 공통으로 겹치는 부분을 도출해서 길이를 구하는 방식
# 최장수열을 구하는 방식이 아닌 최대로 겹치는 공통 문자열을 찾는 방식으로 오답을 도출 할수 있기에 정답이 아님
n = input()
m = input()
a = ['' for i in range(len(n))]

for h in range(len(n)):
    for i in range(h, len(n)):
        for j in range(i, len(m)):
            if n[i] == m[j]:
                a[h] += m[j]
                break

a.sort(key = lambda x:len(x))
print(len(a[-1]))

# 2번 이후 도출한 정답
x = input()
y = input()
a = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]

for i in range(1, len(x) + 1):
    for j in range(1, len(y) + 1):
        if x[i - 1] == y[j - 1]:
            a[i][j] = a[i - 1][j - 1] + 1
        else:
            a[i][j] = max(a[i][j - 1], a[i - 1][j])

print(a[len(x)][len(y)])