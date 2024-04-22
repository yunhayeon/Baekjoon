import sys
input = sys.stdin.readline

def preorder(t):
    if t:
        print(stc[t - 1], end='')
        preorder(left[t])
        preorder(right[t])

def inorder(t):
    if t:
        inorder(left[t])
        print(stc[t - 1], end='')
        inorder(right[t])

def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        print(stc[t - 1], end='')

N = int(input())
left = [0] * (N + 1)
right = [0] * (N + 1)
stc = [chr(i + 65) for i in range(N)]

for _ in range(N):
    p, c1, c2 = input().split()
    i = ord(p) - 64
    if c1 != '.':
        left[i] = ord(c1) - 64
    if c2 != '.':
        right[i] = ord(c2) - 64

preorder(1)
print()
inorder(1)
print()
postorder(1)
print()