from collections import deque
import sys
input = sys.stdin.readline

di = [2, 2, 1, 1, -1, -1, -2, -2]
dj = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())

for _ in range(T):
    l = int(input())
    now = deque([tuple(map(int, input().split()))])
    end = tuple(map(int, input().split()))

    cnt = 0
    visited = [[0 for _ in range(l)] for _ in range(l)]

    if now[0] == end:
        now = []
    else:
        visited[now[0][0]][now[0][1]] = 1

    while now:
        size = len(now)
        cnt += 1

        for _ in range(size):
            i, j = now.popleft()

            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]

                if 0 <= ni < l and 0 <= nj < l and not visited[ni][nj]:
                    if (ni, nj) == end:
                        now = []
                        break

                    now.append((ni, nj))
                    visited[ni][nj] = 1

            if not now:
                break
        
        if  not now:
            break


    print(cnt)
            