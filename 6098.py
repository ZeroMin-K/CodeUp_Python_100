board = []
for _ in range(10):
    board_list = list(map(int, input().split()))
    board.append(board_list)

i = 1
j = 1
board[i][j] = 9
while True:
    if board[i][j+1] == 0:
        board[i][j+1] = 9
        j += 1
    elif board[i][j+1] == 2:
        board[i][j+1] = 9 
        break
    else:
        if board[i+1][j] == 0:
            board[i+1][j] = 9
            i += 1
        elif board[i+1][j] == 2:
            board[i+1][j] = 9
            break
        else:
            break

for k in range(10):
    for l in range(10):
        print(board[k][l], end= ' ')
    print()
