# 백준 11657 - 타임 머신
import sys 
 
N, M = map(int, input().split())
edges = []
distance = [sys.maxsize]*(N+1)

for _ in range(M):  # 에지리스트 저장
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

# 벨만포스 수행
distance[1] = 0

for _ in range(N-1):    # 노드개수 - 1까지 반복
    for start, end, time in edges:
        if distance[start]  != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time

# 음수사이클
mCycle = False
for start, end, time in edges:
    if distance[start]  != sys.maxsize and distance[end] > distance[start] + time:
        # distance[end] = distance[start] + time
        mCycle = True # 음수사이클이 존재 
        break   # 음수 사이클이 있으면 더이상 진행할 필요없음

if mCycle != True :
    for i in range(2,N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:   # 도시에 방문안함
            print(-1)
else:
    print(-1)
