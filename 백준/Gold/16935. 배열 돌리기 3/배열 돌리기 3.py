import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
Rlst = list(map(int, input().split()))

def cal1():
  global lst
  lst.reverse()


def cal2():
  global lst
  for l in lst:
    l.reverse()


def cal3():
  global N, M, lst
  R, C = len(lst), len(lst[0])
  rot = [[0 for _ in range(R)] for _ in range(C)]

  for r in range(R):
    for c in range(C):
      rot[c][R - r - 1] = lst[r][c]

  N, M = M, N
  lst = rot


def cal4():
  global N, M, lst
  R, C = len(lst), len(lst[0])
  rot = [[0 for _ in range(R)] for _ in range(C)]

  for r in range(R):
    for c in range(C):
      rot[C - c - 1][r] = lst[r][c]

  N, M = M, N
  lst = rot


def cal5():
  global lst
  hn, hm = N // 2, M // 2
  newLst = [[0 for _ in range(M)] for _ in range(N)]

  for n in range(N):
    for m in range(M):
      if n < hn and m < hm:
        newLst[n][m + hm] = lst[n][m]
      elif n < hn and m >= hm:
        newLst[n + hn][m] = lst[n][m]
      elif n >= hn and m >= hm:
        newLst[n][m - hm] = lst[n][m]
      elif n >= hn and m < hm:
        newLst[n - hn][m] = lst[n][m]

  lst = newLst


def cal6():
  global lst
  hn, hm = N // 2, M // 2
  newLst = [[0 for _ in range(M)] for _ in range(N)]

  for n in range(N):
    for m in range(M):
      if n < hn and m < hm:
        newLst[n + hn][m] = lst[n][m]
      elif n < hn and m >= hm:
        newLst[n][m - hm] = lst[n][m]
      elif n >= hn and m < hm:
        newLst[n][m + hm] = lst[n][m]
      elif n >= hn and m >= hm:
        newLst[n - hn][m] = lst[n][m]

  lst = newLst


for r in Rlst:
  if r == 1:
    cal1()
  elif r == 2:
    cal2()
  elif r == 3:
    cal3()
  elif r == 4:
    cal4()
  elif r == 5:
    cal5()
  else:
    cal6()


for l in lst:
  print(*l)