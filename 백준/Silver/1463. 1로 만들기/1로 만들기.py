from collections import deque
import sys
input = sys.stdin.readline

d = [2, 3]

N = int(input())
q = deque([N])
visited = [0] * N
flag = 0
cnt = 0

if N != 1:
    while q:
        cnt += 1
        size = len(q)

        for _ in range(size):
            num = q.popleft()

            for i in d:
                n = num // i
                if num % i == 0 and not visited[n]:
                    if n == 1:
                        flag = 1
                        break
                    visited[n] = 1
                    q.append(n)

            if num - 1 != 1:
                visited[num - 1] = 1
                q.append(num - 1)
            else:
                flag = 1
                break

        if flag:
            break


print(cnt)