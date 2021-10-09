h,w = map(int, input().split())
n = int(input())

board = [[0] * w for _ in range(h)]
for _ in range(n):
    l, d, x, y = map(int, input().split())
    x -= 1
    y -= 1
    
    if d == 0:
        for _ in range(l):
            board[x][y] = 1
            y += 1
    else:
        for _ in range(l):
            board[x][y] = 1
            x += 1
            
for i in range(h):
    for j in range(w):
        print(board[i][j], end = ' ')
    print()
