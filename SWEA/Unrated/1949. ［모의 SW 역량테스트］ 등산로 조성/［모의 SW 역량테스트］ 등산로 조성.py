dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c, canBreak, cnt):
    global maxLength
    canGo = False

    # 재귀 호출 조건
    for d in range(4):
        nr, nc = r + dr[d], c + dc[d]
        
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if lst[nr][nc] < lst[r][c]:
                canGo = True
                visited[nr][nc] = 1
                dfs(nr, nc, canBreak, cnt + 1)
                visited[nr][nc] = 0

            elif canBreak and lst[nr][nc] - K < lst[r][c]:
                canGo = True
                visited[nr][nc] = 1
                past = lst[nr][nc]
                lst[nr][nc] = lst[r][c] - 1
                dfs(nr, nc, 0, cnt + 1)
                visited[nr][nc] = 0
                lst[nr][nc] = past

    # 종료 조건
    if not canGo:
        if cnt > maxLength:
            maxLength = cnt
        return

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    top = 0         # 봉우리 높이
    topLst = []     # 봉우리 좌표 리스트
    maxLength = 0   # 최장 길이

    # 최고 높이의 봉우리를 찾고 그 좌표를 저장
    for i in range(N):
        for j in range(N):
            if lst[i][j] > top:
                top = lst[i][j]
                topLst = [(i, j)]
            elif lst[i][j] == top:
                topLst.append((i, j))

    # 봉우리별 최장 길이 계산
    for si, sj in topLst:
        visited = [[0] * N for _ in range(N)]
        visited[si][sj] = 1
        dfs(si, sj, 1, 1)

    print(f'#{tc} {maxLength}')