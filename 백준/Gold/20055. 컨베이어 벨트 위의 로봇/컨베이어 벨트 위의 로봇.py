from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))
robot = deque([0] * (N * 2))
cnt = 0

while True:
    # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    belt.appendleft(belt.pop())
    robot.appendleft(robot.pop())
    if robot[N - 1] == 1:
        robot[N - 1] = 0

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 
    #    만약 이동할 수 없다면 가만히 있는다.
    for i in range(N - 1, 1, -1):
        if robot[i - 1] == 1 and robot[i] == 0 and belt[i] > 0:
            robot[i - 1] = 0
            robot[i] = 1
            belt[i] -= 1
    if robot[N - 1] == 1:
        robot[N - 1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1

    cnt += 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if belt.count(0) >= K:
        break

print(cnt)