import sys

while True: 
  try:
    s, t = sys.stdin.readline().split()

    cnt = 0
    for i in range(len(t)):
      if cnt < len(s) and s[cnt] == t[i]:
        cnt += 1

    if cnt == len(s):
      print('Yes')
    else:
      print('No')

  except ValueError: 
    break