# 보드판 입력받
from collections import deque

board = []
for i in range(7):
    board.append(input().split())

# queue = deque([board[0][0]])
queue = deque((0, 0))
# 방문 기록
record = [[False] * 7 for _ in range(7)]
record[0][0] = True

while queue:
    x_y = queue.pop()
    x = x_y[0]
    y = x_y[1]
    color = board[x][y]

    # num과 인접한 애들 탐
    for i in range(1, 3):
        if not record[x][y+i]:
            queue.append(board[x][y+i])
            record[x][y+i] = True
        if not record[x+i][y]:
            queue.append(board[x+i][y])
            record[x+i][y] = True