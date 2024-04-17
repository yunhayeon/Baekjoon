import sys
input = sys.stdin.readline

N, M, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
enemy = []
attack = [i for i in range(M)]
dieEnemyCnt = [0]

for r in range(N):
    for c in range(M):
        if lst[r][c] == 1:
            enemy.append((r, c))


def attackEnemy(attacker, en, dieEnemy):
    realAttack = []

    for a in attacker:
        ai, aj = a
        minDis = -1
        aCanAttack = []

        for e in en:
            ei, ej = e

            dis = (ai - ei) + abs(aj - ej)
            if dis <= D:
                if minDis == -1:
                    minDis = dis
                    aCanAttack.append((ei, ej))
                else:
                    if minDis > dis:
                        minDis = dis
                        aCanAttack = [(ei, ej)]
                    elif minDis == dis:
                        aCanAttack.append((ei, ej))

        aCanAttack.sort(key= lambda x:x[1])
        if aCanAttack:
            realAttack.append(aCanAttack[0])

    realAttack = list(set(realAttack))

    survive = []
    for e in en:
        if e not in realAttack:
            r, c = e
            if r + 1 != N:
                survive.append((r + 1, c))

    if survive:
        attackEnemy(attacker, survive, dieEnemy + len(realAttack))
    else:
        dieEnemyCnt.append(dieEnemy + len(realAttack))

                            
def perm(level, idx, used):
    if level == 3:
        attacker = []
        for u in used:
            attacker.append((N, u))
        attackEnemy(attacker, enemy, 0)

    for i in range(idx, M):
        perm(level + 1, i + 1, used + [attack[i]])


perm(0, 0, [])
print(max(dieEnemyCnt))