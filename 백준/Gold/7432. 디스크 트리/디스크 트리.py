import sys
input = sys.stdin.readline

N = int(input())
tree = {}
keys = []

for _ in range(N):
  lst = input().rstrip().split('\\')

  if lst[0] not in tree:
    keys.append(lst[0])
    tree[lst[0]] = [lst[1:]]
  else:
    tree[lst[0]].append(lst[1:])

keys.sort()

for key in keys:
  print(key)

  lst = tree[key]
  lst.sort()

  for i in range(len(lst)):
    now = lst[i]
    past = lst[i - 1] if i else []
    pl = len(past)

    for j in range(len(now)):
      if pl and pl > j:
        if now[j] == past[j]:
          continue
        else:
          pl = 0

      print(f'{" " * (j + 1)}{now[j]}')