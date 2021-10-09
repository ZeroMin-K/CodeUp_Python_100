board = []
for _ in range(19):
    board_list = list(map(int, input().split()))
    board.append(board_list)
    
n= int(input())

for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    for i in range(19):
        if board[x][i] == 1:
            board[x][i] = 0
        else:
            board[x][i] = 1
            
    for j in range(19):
        if board[j][y] == 1:
            board[j][y] = 0
        else:
            board[j][y] = 1

for k in range(19):
    for l in range(19):
        print(board[k][l], end = ' ')
    print()
