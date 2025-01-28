import sys
input = sys.stdin.readline

di = [0, 0, 0, -1, 1]
dj = [0, 1, -1, 0, 0]

# 위, 북, 동, 서, 남, 아래
dice = [0 for _ in range(6)]

N, M, i, j, _ = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))

def roll(d):
  global dice

  if d == 1:
    dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
  elif d == 2:
    dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
  elif d == 3:
    dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
  elif d == 4:
    dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]


for d in orders:
  ni, nj = i + di[d], j + dj[d]

  if 0 <= ni < N and 0 <= nj < M:
    roll(d)

    if lst[ni][nj] == 0:
      lst[ni][nj] = dice[5]

    else:
      dice[5] = lst[ni][nj]
      lst[ni][nj] = 0

    print(dice[0])

    i, j = ni, nj
