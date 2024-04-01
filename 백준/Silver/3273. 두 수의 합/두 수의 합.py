import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
num = int(input())
cnt = 0

def perm(level, idx, total):
    global cnt

    if level == 2:
        if total == num:
            cnt += 1
        return
    

    for i in range(idx, N):
        if (not total and lst[i] < num) or (total + lst[i] == num):
            perm(level + 1, i + 1, total + lst[i])

perm(0, 0, 0)

print(cnt)