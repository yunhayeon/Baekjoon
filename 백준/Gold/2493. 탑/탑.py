import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = [0 for _ in range(N)]
st = []

for n in range(N):
  for i in range(len(st) - 1, - 1, - 1):
    if st[i][1] > lst[n]:
      ans[n] = st[i][0] + 1
      break
    else:
      st.pop()

  st.append((n, lst[n]))

print(*ans)