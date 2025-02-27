import sys
input = sys.stdin.readline

N = int(input())
st = []
ans = 0

for _ in range(N):
  lst = list(map(int, input().rstrip().split(' ')))
  
  if lst[0]:
    lt = lst[2] - 1
    if lt:
      st.append([lst[1], lt])
    else:
      ans += lst[1]
  else:
    if st:
      st[-1][1] -= 1
      if not st[-1][1]:
        ans += st[-1][0]
        st.pop()

print(ans)