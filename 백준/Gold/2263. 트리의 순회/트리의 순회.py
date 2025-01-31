import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
inordDict = {v: i for i, v in enumerate(inOrder)}

def recursion(il, ir, pl, pr):
    if il > ir or pl > pr:
        return
    
    root = postOrder[pr]
    print(root, end=' ')

    rootIdx = inordDict[root]
    postStd = rootIdx - il

    recursion(il, rootIdx - 1, pl, pl + postStd - 1)
    recursion(rootIdx + 1, ir, pl + postStd, pr - 1)

recursion(0, N - 1, 0, N - 1)