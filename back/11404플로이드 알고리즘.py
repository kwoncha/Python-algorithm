# 처음에 트리를 구성해 dfs, bfs 방식을 떠올렸지만 실패
INF = float('inf')

n = int(input())
m = int(input())
# 2차원 리스트를 만들고 초기화
arr= [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신으로 가는건 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n+1):
        if i ==j:
            arr[i][j] = 0
            
# 간선의 정보를 입력받아 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
#     가장 작은 값만 입력되도록 함
    arr[a][b] = min(arr[a][b], c)
    
# 플로이드 워셜 알고리즘, 노드 사이에 최단 거리를 구하는 알고리즘
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
#            직행으로 가는 것과 그러지 않은것 중에 최솟값을 입력
            arr[a][b] = min(arr[a][b],  arr[a][k] + arr[k][b])
            
for a in range(1, n+1):
    for b in range(1, n+1):
        if arr[a][b] == INF:
            print(0, end=' ')
        else:
            print(arr[a][b], end=' ')
    print()
    