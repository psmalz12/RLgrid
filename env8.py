ROWS = 7
COLS = 7
Goal = (1, 5)
walls = [(2,5),(2,4),(2,3), (3,2)]


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
        self.state=(5,1)
        return self.state


    def action (self):
        pass
        #if self.state != 1, 3:
        #herei neet to creat a lop (with random.choice meth i have to chek book at 156,157)


    def agentmove(self, dest):
        # the current loc of the agent
        col, row = self.state

        # update the loc based on the direction/destination
        if dest == "left":
            new_col =col - 1
            new_row = row
        elif dest == "right":
            new_col = col + 1
            new_row = row
        elif dest == "up":
            new_cpol = col
            new_row = row +1
        elif dest == "down":
            new_col = col
            new_row = row - 1

        # check if the new position is valid (not a wall "!=1" and within the grid 0-col/rows)
        if 0 <= new_col < COLS and 0 <= new_row < ROWS and self.board[new_row][new_col] != 1:
            # Update the state of the agent
            self.state = (new_col, new_row)

        # return the new location(state) of the agent
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


grid = Grid(state=(5, 1))

if __name__ == "__main__":
    grid.showBoard()

# this hiw i imagin the grid
#[0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]
#[1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
#[2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
#[3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
#[4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
#[5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
#[6][0] [6][1] [6][2] [6][3] [6][4] [6][5] [6][6]
