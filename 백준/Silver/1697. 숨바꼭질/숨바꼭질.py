from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 200001
visited[N] = 1
q = deque([N])
cnt = 0
flag = 0

d = [-1, 1]

if N != K:
    while q:
        cnt += 1
        size = len(q)

        for _ in range(size):
            idx = q.popleft()

            for i in d:
                m = idx + i
                if 0 <= m <= 100000 and not visited[m]:
                    if m == K:
                        flag = 1
                        break
                    visited[m] = 1
                    q.append(m)

            x = idx * 2
            if 0 <= x <= 100000 and not visited[x]:
                if x == K:
                    flag = 1
                    break
                visited[x] = 1
                q.append(x)
        
        if flag:
            break

print(cnt)