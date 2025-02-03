import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  n = int(input())
  lst = [input().rstrip() for _ in range(n)]
  lst.sort()
  ans = 'YES'
  
  for i in range(n):
    l = len(lst[i])
    for j in range(i + 1, n):
      if lst[i] == lst[j][:l]:
        ans = 'NO'
        break
    
    if ans == 'NO':
      break

  print(ans)
