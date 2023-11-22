# 그리디 문제, 정렬을 이용해 해결
# 결과적으로 정렬을해 차이가 많이 나는 것들을 제외한 합이 정답

n = int(input())
m = int(input())
sen = list(map(int, input().split()))
sen.sort()
result, count = [], 0
for i in range(len(sen)-1):
    result.append(sen[i+1] - sen[i])

result.sort()
a = result[:len(result)- m +1]

print(sum(a))