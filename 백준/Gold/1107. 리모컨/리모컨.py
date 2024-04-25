import sys
input = sys.stdin.readline

target = int(input())
brokenN = int(input())
btn = [i for i in range(10)]
if brokenN:
    broken = set(list(map(int, input().split())))
    btn = list(set(btn) - broken)

targetLen = len(str(target))
btnLen = len(btn)
minDif = 500000
ans = 0
length = 0

def perm(level, end, used):
    global minDif, length

    if level == end:
        dif = abs(int(used) - target)
        if minDif > dif:
            minDif = dif
            length = end
        return
    
    if minDif != 0:
        for i in range(btnLen):
            if not (end != 1 and len(used) == 0 and btn[i] == 0):
                perm(level + 1, end, used + f'{btn[i]}')

if target != 100:
    if target > 9:
        perm(0, targetLen - 1, '')
    perm(0, targetLen, '')
    perm(0, targetLen + 1, '')
    ans = minDif + length

    pm = abs(target - 100)
    if ans > pm:
        ans = pm

print(ans)