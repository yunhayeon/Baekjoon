import sys
input = sys.stdin.readline

K = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(K)]
order = '0'

for i in range(1, K):
    order = f'{i}' + f'{i}'.join(list(order)) + f'{i}'

order = list(map(int, list(order)))

for i in range(len(lst)):
    tree[order[i]].append(lst[i])

for t in tree:
    print(*t)
