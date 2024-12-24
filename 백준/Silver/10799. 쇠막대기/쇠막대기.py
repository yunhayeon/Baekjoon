import sys
input = sys.stdin.readline

lst = list(input().rstrip())
st = []
ans = 0

for i in range(len(lst)):
  if lst[i] == '(':
    st.append('(')
  elif lst[i] == ')':
    st.pop()
    if lst[i - 1] == '(':
      ans += len(st)
    else:
      ans += 1

print(ans)
