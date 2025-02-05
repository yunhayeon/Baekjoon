import sys
input = sys.stdin.readline

N = int(input())
tree = {}
keys = []
dash = '--'
out = []

for _ in range(N):
  lst = list(input().split())

  if lst[1] not in tree:
    keys.append(lst[1])
    tree[lst[1]] = [lst[2:]]
  else:
    tree[lst[1]].append(lst[2:])

keys.sort()

for key in keys:
  out.append(f"{key}\n")
  tree[key].sort()

  for i in range(len(tree[key])):
    n = 0
    past, pl = [], 0
    check = False

    if i:
      past = tree[key][i - 1]
      pl = len(past)

    now = tree[key][i]
    nl = len(now)

    if pl:
      check = True

    for j in range(nl):
      n += 1
      if check:
        if j < pl and past[j] == now[j]:
          continue
        else:
          check = False
          
      out.append(f"{dash * n}{tree[key][i][j]}\n")

sys.stdout.write("".join(out))