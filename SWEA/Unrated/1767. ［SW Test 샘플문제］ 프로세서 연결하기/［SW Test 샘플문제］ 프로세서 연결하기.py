di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# idx : 탐색하고 있는 프로세서
# used : 사용한 프로세서 개수
def possible_direction(idx, used):
    global used_max
    global total

    # 1. 기저 조건
    if idx == size:
        # 전보다 더 많은 프로세서를 사용했다면
        if used >= used_max:
            cnt = - p_cnt
            for rn in range(N):
                for cn in range(N):
                    if visited[rn][cn] == 1:
                        cnt += 1
            if used == used_max:
                total = min(total, cnt)
            else:
                used_max = used
                total = cnt

        return
    
    # 2. 재귀 호출 조건
    r, c = q[idx]
    for d in range(4):
        k = 0
        road = []

        while True:
            k += 1
            nr, nc = r + di[d] * k, c + dj[d] * k

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 0:
                    road.append((nr, nc))
                else:
                    road = []
                    break
            else:
                break

        # 연결 가능한 방향이 있다면
        if road:
            for i, j in road:
                visited[i][j] = 1

            possible_direction(idx + 1, used + 1)

            for i, j in road:
                visited[i][j] = 0

    # 아무 방향으로도 연결하지 않았을 때
    else:
        possible_direction(idx + 1, used)
        

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    p_cnt = 0         # 총 프로세서 개수
    q = []            # 프로세서 좌표 리스트(가장자리 제외)
    used_max = 0      # 사용한 최대 프로세서 수
    total = 144       # 최대 프로세서 사용 시 전선 길이의 최소 합

    # 프로세서 좌표 찾고
    # 프로세서 좌표 방문 처리
    # 가장자리가 아닌 프로세서의 좌표 q 리스트에 담기
    for i in range(N):
        for j in range(N):
            if lst[i][j] == 1:
                p_cnt += 1
                visited[i][j] = 1
                if 0 < i < N - 1 and 0 < j < N - 1:
                    q.append((i, j))

    # 탐색할 프로세서 개수(재귀 호출 종료 조건에 사용)
    size = len(q)

    possible_direction(0, 0)

    print(f'#{tc} {total}')