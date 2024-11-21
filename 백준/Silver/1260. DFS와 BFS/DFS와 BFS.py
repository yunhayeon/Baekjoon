import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
lst = [[] for _ in  range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    lst[i].append(j)
    lst[j].append(i)

for i in range(N + 1):
    lst[i].sort()


def dfs(s):
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    stack = [s]
    ans = [s]
    now = s

    while stack:
        for next in lst[now]:
            if not visited[next]:
                stack.append(now)
                visited[next] = 1
                ans.append(next)
                now = next
                break
        else:
            if stack:
                now = stack.pop()
            else:
                break

    return ans


def bfs(s):
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    q = [s]
    ans = [s]
    
    while q:
        now = q.pop(0)

        for next in lst[now]:
            if not visited[next]:
                q.append(next)
                ans.append(next)
                visited[next] = 1
    
    return ans


print(*dfs(V))
print(*bfs(V))