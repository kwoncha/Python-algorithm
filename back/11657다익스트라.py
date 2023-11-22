import sys
input = sys.stdin.readline


#벨만 포드 알고리즘 구현 함수 
def bf(start):

    dist[start]=0
    #전체 n번의 라운드를 반복
    for i in range(n):
        #매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur = result[j][0]
            nex = result[j][1]
            cost = result[j][2]

            #현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur]!=1e9 and dist[nex]>dist[cur]+cost:
                dist[nex] = dist[cur]+cost
                #n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i==n-1:
                    return True
    return False
            
n,m = map(int,input().split())
result=[]
dist = [1e9]*(n+1)

for i in range(m):
    a,b,c = map(int,input().split())
    result.append([a,b,c])

#벨만 포드 알고리즘을 수행
answer = bf(1) #1번 노드가 시작 노드

if answer: #음수 순환이 존재하면
    print("-1")
else:
    for i in range(2,n+1):
        #도달할 수 없는 경우 -1출력
        if dist[i]==1e9:
            print("-1")
        #도달할 수 있는 경우 거리 출력  
        else:
            print(dist[i])