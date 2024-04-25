from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = list(input().rstrip())
    n = int(input())
    lst = input()[1:-2]
    if lst:
        lst = deque(list(map(int, lst.split(','))))
    else:
        lst = deque([])

    error = False
    rev = 0
    
    for p in P:
        if p == 'R':
            rev = (rev + 1) % 2

        else:
            if lst:
                if rev:
                    lst.pop()
                else:
                    lst.popleft()
            else:
                error = True
                break

    if rev:
        lst.reverse()

    if error:
        print('error')
    else:
        lst = str(lst).replace(' ', '')[6:-1]
        print(lst)