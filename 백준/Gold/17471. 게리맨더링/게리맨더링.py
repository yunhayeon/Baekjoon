from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
people = list(map(int, input().split()))
lst = [[] for _ in range(N + 1)]
visited = [0] * N
ans = -1

for n in range(1, N + 1):
    part = list(map(int, input().split()))

    for i in range(1, part[0] + 1):
        lst[n].append(part[i])


def bfs(lst, team, v):
    q = deque([v])
    visit = [0] * (N + 1)
    visit[v] = 1
    canGo = []

    while q:
        now = q.popleft()
        
        canGo.append(now)

        for next in lst[now]:
            if not visit[next] and next in team:
                q.append(next)
                visit[next] = visit[now] + 1

    if sorted(canGo) == team:
        return True
    else:
        return False
        

def teamCheck(visited):
    global ans

    teamA = []
    teamB = []
    for i in range(N):
        if visited[i]:
            teamA.append(i + 1)
        else:
            teamB.append(i + 1)
        
    if bfs(lst, teamA, teamA[0]) and bfs(lst, teamB, teamB[0]):
        # 인구수 차이 계산
        peopleA = 0
        peopleB = 0
        for j in range(N):
            if visited[j]:
                peopleA += people[j]
            else:
                peopleB += people[j]

        dif = abs(peopleA - peopleB)
        if ans == -1:
            ans = dif
        else:
            if ans > dif:
                ans = dif

    
def perm(level, idx, end):
    if level == end:
        teamCheck(visited)
        return
    
    for i in range(idx, N):
        visited[i] = 1
        perm(level + 1, i + 1, end)
        visited[i] = 0

for e in range(1, N // 2 + 1):
    if ans != 0:
        perm(0, 0, e)

print(ans)