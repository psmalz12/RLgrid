ROWS = 7
COLS = 7
Goal = (1, 5)
walls = [(2,5),(2,4),(2,3), (3,2)]

# solved the move agent fun it was an axis issue 20/03/2024
# now i might think of random acrion fun and how updated the state velue?

class Grid:
    def __init__(self, state):
        self.state = state
        self.board = []

        for x in range(ROWS):
            row = []
            for y in range(COLS):
                if (x == 0 or y == 0 or x == ROWS - 1 or y == COLS - 1) or (x, y) in walls:
                    row.append(1)  # walls & border
                elif (x, y) == Goal:
                    row.append(3)
                else:
                    row.append(0)  # empty cells
            self.board.append(row)



    def reset(self):
       # self.state=(5,1)
        return self.state


    def action (self):
        pass

    def agentmove(self, dest):
        # Current position of the agent
        x, y = self.state
        # update the position based on the direction fcol = "future column"
        # x > rep the row / y > rep the col
        if dest == "left":
            fcol = x
            frow = y - 1
        elif dest == "right":
            fcol = x
            frow = y + 1
        elif dest == "up":
            fcol = x - 1
            frow = y
        elif dest == "down":
            fcol = x + 1
            frow = y
        else:
            # invalid direction agent stay in same position
            fcol = x
            frow = y
        print(f'//////// agent Moving : {dest} ////////')

        # check if the new position is valid (not a wall and within the grid)
        if self.board[fcol][frow] != 1:
            # Update the state of the agent
            self.state = (fcol, frow)
            print(f'//////// agent current Location : {self.state} ////////')
        else:
            print('Faced an Obstacle')
            print(f'//////// agent current Location : {self.state} ////////')


        # Return the new state of the agent
        return self.state

    def showBoard(self):
        for x in range(1, ROWS - 1):
            print('----------------------')
            out = '| '
            for y in range(1, COLS - 1):
                if (x, y) == self.state:
                    out += '2 | '  # 2 for the robot location
                elif self.board[x][y] == 3:
                    out+= 'G | ' # for the goal cell
                elif self.board[x][y] == 1:
                    out += '# | '  # draw # for walls or obstacles
                elif self.board[x][y] == 0:
                    out += '  | '  #  0  == 'space' for empty cell
            print(out)
        print('-----------------------')



if __name__ == "__main__":
    grid = Grid(state=(5, 1))
    print('//////// agent current Location "2" ////////')
    grid.showBoard()
    grid.agentmove("left")
    grid.showBoard()
    grid.agentmove("right")
    grid.agentmove("right")
    grid.showBoard()
    grid.agentmove("up")
    grid.agentmove("up")
    grid.showBoard()
    grid.agentmove("down")
    grid.showBoard()
    grid.agentmove("left")
    grid.showBoard()



# this hiw i imagin the grid
#[0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]
#[1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
#[2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
#[3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
#[4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
#[5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
#[6][0] [6][1] [6][2] [6][3] [6][4] [6][5] [6][6]
