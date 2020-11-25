#[up,down,left,right]

class Ball:
    def __init__(self,i,j,dir1,dir2):
        self.pos = (i,j)
        self.dir = (dir1,dir2)

    def update(self,vert,hori):
        up = self.dir[1]
        up += vert
        side = self.dir[0]
        side += hori
        self.dir = (side,up)


class Board:
    def __init__(self,n):
        self.n = n
        self.board = [[0 for i in range(n)]for j in range(n)]

    def initialise(self):
        self.board[0],self.board[-1] = [1 for i in range(self.n)], [1 for i in range(self.n)]
        for i in range(self.n):
            self.board[i][0] = 1
            self.board[i][-1] = 1

    def print_board(self):
        for i in range(self.n):
            print(self.board[i])

    def get_neighbours(self,i,j):
        ret = [None,None,None,None]
        if self.board[j-1][i] != 0:
            ret[0] = 1
        if self.board[j+1][i] != 0:
            ret[1] = 1
        if self.board[j][i-1] != 0:
            ret[2] = 1
        if self.board[j][i+1] != 0:
            ret[3] = 1
        return ret

    def place_ball(self,ball):
        i,j = ball.pos
        self.board[j][i] = ball

    def next_ite(self):
        pass
    


a = Board(10)
b = Ball(1,1,1,1)
a.initialise()
a.place_ball(b)
a.print_board()
print(a.get_neighbours(a.n-2,1))
