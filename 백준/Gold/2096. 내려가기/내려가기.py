import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))

maxi = lst
mini = lst

for _ in range(N - 1):
    i0, i1, i2 = map(int, input().split())

    maxi = [i0 + max(maxi[0], maxi[1]), i1 + max(maxi), i2 + max(maxi[1], maxi[2])]
    mini = [i0 + min(mini[0], mini[1]), i1 + min(mini), i2 + min(mini[1], mini[2])]

print(max(maxi), min(mini))