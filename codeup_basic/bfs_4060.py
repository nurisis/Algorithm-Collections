from collections import deque

m, n = input().split()
m = int(m)
n = int(n)

board = []
board_2 = []
for i in range(m):
    array = input().split()
    board.append(array.copy())
    board_2.append(array.copy())

# 방문 기록
record = [[False] * n for _ in range(m)]

num_of_turn_off, num_of_turn_on = 0, 0

# 모든 전구를 켜기 위한. 0 -> 1
for i in range(m):
    for j in range(n):
        if board[i][j] == '0':
            num_of_turn_on += 1

            queue_inside = deque()
            queue_inside.append((i, j))
            record[i][j] = True
            board[i][j] = '1'

            while queue_inside:
                matrix = queue_inside.pop()
                x = matrix[0]
                y = matrix[1]

                # 상
                if x > 0 and not record[x - 1][y] and board[x - 1][y] != '1':
                    # 전구 켜줌
                    board[x - 1][y] = '1'
                    # 방문 기록
                    record[x - 1][y] = True
                    # queue 삽입
                    queue_inside.append((x - 1, y))
                # 하
                if x < m - 1 and not record[x + 1][y] and board[x + 1][y] != '1':
                    # 전구 켜줌
                    board[x + 1][y] = '1'
                    # 방문 기록
                    record[x + 1][y] = True
                    # queue 삽입
                    queue_inside.append((x + 1, y))
                # 좌
                if y > 0 and not record[x][y - 1] and board[x][y - 1] != '1':
                    # 전구 켜줌
                    board[x][y - 1] = '1'
                    # 방문 기록
                    record[x][y - 1] = True
                    # queue 삽입
                    queue_inside.append((x, y - 1))
                # 우
                if y < n - 1 and not record[x][y + 1] and board[x][y + 1] != '1':
                    # 전구 켜줌
                    board[x][y + 1] = '1'
                    # 방문 기록
                    record[x][y + 1] = True
                    # queue 삽입
                    queue_inside.append((x, y + 1))

# 모든 전구를 끄 위한. 1 -> 0

# 방문 기록
record = [[False] * n for _ in range(m)]

# print("*** board_2 : ")
# for i in range(m): print(board_2[i])
# print("**** record")
# print(record)

for i in range(m):
    for j in range(n):
        if board_2[i][j] == '1':
            num_of_turn_off += 1

            queue_inside = deque()
            queue_inside.append((i, j))
            record[i][j] = True
            board_2[i][j] = '0'

            while queue_inside:
                matrix = queue_inside.pop()
                x = matrix[0]
                y = matrix[1]

                # 상
                if x > 0 and not record[x - 1][y] and board_2[x - 1][y] != '0':
                    # 전구 켜줌
                    board_2[x - 1][y] = '0'
                    # 방문 기록
                    record[x - 1][y] = True
                    # queue 삽입
                    queue_inside.append((x - 1, y))
                # 하
                if x < m - 1 and not record[x + 1][y] and board_2[x + 1][y] != '0':
                    # 전구 켜줌
                    board_2[x + 1][y] = '0'
                    # 방문 기록
                    record[x + 1][y] = True
                    # queue 삽입
                    queue_inside.append((x + 1, y))
                # 좌
                if y > 0 and not record[x][y - 1] and board_2[x][y - 1] != '0':
                    # 전구 켜줌
                    board_2[x][y - 1] = '0'
                    # 방문 기록
                    record[x][y - 1] = True
                    # queue 삽입
                    queue_inside.append((x, y - 1))
                # 우
                if y < n - 1 and not record[x][y + 1] and board_2[x][y + 1] != '0':
                    # 전구 켜줌
                    board_2[x][y + 1] = '0'
                    # 방문 기록
                    record[x][y + 1] = True
                    # queue 삽입
                    queue_inside.append((x, y + 1))

print(num_of_turn_on, num_of_turn_off)