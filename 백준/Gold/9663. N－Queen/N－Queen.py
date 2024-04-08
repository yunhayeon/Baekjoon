import sys
input = sys.stdin.readline

def cross(target, used):
    for i in range(1, len(used) + 1):
        if abs(target - used[-i]) == i:
            return False
    else:
        return True

def perm(level, used):
    global cnt
    if level == N:
        cnt += 1
        return
    
    for i in range(N):
        if not visited[i] and (not used or (used and abs(lst[i] - used[-1]) > 1)) and cross(lst[i], used):
            visited[i] = 1
            perm(level + 1, used + [lst[i]])
            visited[i] = 0


N = int(input())
lst = [i for i in range(1, N + 1)]
visited = [0] * N
cnt = 0

perm(0, [])

print(cnt)