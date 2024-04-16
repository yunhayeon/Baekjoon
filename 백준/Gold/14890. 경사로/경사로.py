import sys
input = sys.stdin.readline

N, L = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    part = [lst[i][0]]
    check = 0

    for j in range(1, N):
        if lst[i][j] == part[-1]:
            part.append(lst[i][j])
        
        elif lst[i][j] - 1 == part[-1]:
            if check == 0:
                if len(part) >= L:
                    part = [lst[i][j]]
                else:
                    break
            else:
                if len(part) >= L * 2:
                    check = 0
                    part = [lst[i][j]]
                else:
                    break
            
        elif lst[i][j] + 1 == part[-1]:
            if check == 0:
                check = 1
                part = [lst[i][j]]
            else:
                if len(part) >= L:
                    part = [lst[i][j]]
                else:
                    break

        else:
            break

        if j == N - 1:
            if check and len(part) < L:
                break
            ans += 1


for j in range(N):
    part = [lst[0][j]]
    check = 0

    for i in range(1, N):
        if lst[i][j] == part[-1]:
            part.append(lst[i][j])
        
        elif lst[i][j] - 1 == part[-1]:
            if check == 0:
                if len(part) >= L:
                    part = [lst[i][j]]
                else:
                    break
            else:
                if len(part) >= L * 2:
                    check = 0
                    part = [lst[i][j]]
                else:
                    break
            
        elif lst[i][j] + 1 == part[-1]:
            if check == 0:
                check = 1
                part = [lst[i][j]]
            else:
                if len(part) >= L:
                    part = [lst[i][j]]
                else:
                    break

        else:
            break
        
        if i == N - 1:
            if check and len(part) < L:
                break
            ans += 1


print(ans)