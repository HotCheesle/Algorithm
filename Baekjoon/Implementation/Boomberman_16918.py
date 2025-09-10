class Board: 
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    def __init__(self, R, C, board):
        self.bombs = list(list(0 for _ in range(C)) for _ in range(R))
        self.R = R
        self.C = C
        for row in range(R): 
            for col in range(C): 
                if board[row][col] == 'O': 
                    self.bombs[row][col] = 4

    def one_sec_later(self): 
        for row in range(R): 
            for col in range(C): 
                if self.bombs[row][col]: 
                    self.bombs[row][col] -= 1
    
    def boom(self): 
        boom_list = []
        for row in range(self.R): 
            for col in range(self.C): 
                if self.bombs[row][col] == 1: 
                    boom_list.append((row, col))
        for row, col in boom_list: 
            self.bombs[row][col] = 0
            for r, c, in zip(Board.dr, Board.dc): 
                nrow, ncol = row+r, col+c
                if 0 <= nrow < self.R and 0 <= ncol < self.C: 
                    self.bombs[nrow][ncol] = 0
    
    def bomb_has_been_planted(self): 
        for row in range(self.R): 
            for col in range(self.C): 
                if self.bombs[row][col] == 0:
                    self.bombs[row][col] = 4 
    
    def show_board(self): 
        for row in range(self.R): 
            for col in range(self.C): 
                if self.bombs[row][col]:
                    print('O', end='')
                else: 
                    print('.', end='')
            print()

R, C, N = map(int, input().split())
init_board = list(input() for _ in range(R))
bombs = Board(R, C, init_board)
bombs.one_sec_later()
bombs.one_sec_later()
bombs.bomb_has_been_planted()
for time in range(N-2): 
    bombs.one_sec_later()
    bombs.bomb_has_been_planted()
    bombs.boom()
bombs.show_board()