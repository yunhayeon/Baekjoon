import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

visited = [0] * (N + 1)
stack = [(1, 0)]
lastNode = 0

while stack:
    node, depth = stack.pop()
    visited[node] = 1

    if node != 1 and len(tree[node]) == 1:
        lastNode += depth
        
    else:
        for i in tree[node]:
            if not visited[i]:
                stack.append((i, depth + 1))

if lastNode % 2:
    print('Yes')
else:
    print('No')