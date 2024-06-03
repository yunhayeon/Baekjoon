import sys, itertools
input = sys.stdin.readline

r, c, k = map(int, input().split())
lst = []
time = 0
ans = 0

r -= 1
c -= 1

for _ in range(3):
    lst.append(list(map(int, input().split())))

# 계산 결과 저장
def saveNew(new, maxLen):
    for n in range(len(new)):
        while len(new[n]) < maxLen:
            new[n].append(0)
        lst[n] = new[n]

# 연산
def calc():
    new = []
    maxLen = 0

    for l in lst:
        setL = set(l)
        part = []
        for s in setL:
            if s != 0:
                part.append([s, l.count(s)])

        part.sort(key = lambda x : (x[1], x[0]))
        part = list(itertools.chain(*part))
        if len(part) > 100:
            part = part[:100]
        new.append(part)

        if maxLen < len(part):
            maxLen = len(part)

    saveNew(new, maxLen)

# 행 열 변환
def changeCtoR(lst):
    change = []

    for i in range(len(lst[0])):
        cpart = []
        for j in range(len(lst)):
            cpart.append(lst[j][i])
        change.append(cpart)

    return change
    

while True:
    if time > 100:
        ans = -1
        break

    if r < len(lst) and c < len(lst[0]) and lst[r][c] == k:
        ans = time
        break

    # R 연산
    if len(lst[0]) <= len(lst):
        calc()
    # C 연산
    else:
        lst = changeCtoR(lst)
        calc()
        lst = changeCtoR(lst)

    time += 1

print(ans)