from collections import deque
import sys
input = sys.stdin.readline

wheel = []
for _ in range(4):
    wheel.append(deque(list(input().rstrip())))

K = int(input())
for _ in range(K):
    idx, direction = map(int, input().split())

    q = [(idx - 1, direction)]
    visited = [0] * 4

    # 돌아갈 예정인 톱니바퀴 찾기
    while q:
        i, d = q.pop()
        visited[i] = d

        ri = i + 1
        if ri < 4 and visited[ri] == 0 and wheel[i][2] != wheel[ri][6]:
            q.append((ri, -d))

        li = i - 1
        if li > -1 and visited[li] == 0 and wheel[i][6] != wheel[li][2]:
            q.append((li, -d))

    # 돌아가는 톱니바퀴 돌리기
    for v in range(4):
        if visited[v] == 1:
            wheel[v].insert(0, wheel[v].pop())

        elif visited[v] == -1:
            wheel[v].append(wheel[v].popleft())

cnt = 0
for j in range(4):
    if wheel[j][0] == '1':
        cnt += 2 ** j

print(cnt)