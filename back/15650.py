# combinations로 한번에 오름차순 정렬된 것만 뽑기도 가능함
from itertools import permutations
n, m = map(int, input().split())
arr = [i+1 for i in range(n)]
arrs = permutations(arr, m)

sorted_perms = [i for i in arrs if tuple(sorted(i)) == i]
# if sorted(i) == list(i): 이런방식으로도 확인 가능
for i in sorted_perms:
    for j in i:
        print(j, end=' ')
    print()