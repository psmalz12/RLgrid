
ROWS = 5
COLS = 5
WIN_STATE = (1, 5)
# LOSE_STATE = (2, 4) can def this later as loss -1 for RL learning


class Grid:
    def __init__(self, state): # init the grid with one arg that the agent ini state where
        self.state = state # assigns the initial state
        self.board = [] # 2d list represents the entire grid will stor all the cel in the end of the loop
        for _ in range(ROWS + 2): # than loop tp creat a rows + added 2 for boarder 1 in each side
            row= [] # creat a list for each rows to appand a value later
            for _ in range(COLS + 2): # inner loop for cols
                row.append(0) # now appand the 0 to the empty list of row for each col
            self.board.append(row)
        # Set obstacle here we i can def lose state
        self.board[3][2] = "x"

        # fill border columns "x" with 1 to drow a boundry of the grid world (5x5)
        for x in range(ROWS + 2):
            self.board[x][0] = self.board[x][COLS + 1] = 1


            # fill border rows "y" with 1
        for y in range(COLS + 2):
            self.board[0][y] = self.board[ROWS + 1][y] = 1


    def agentmove(self):
       pass

    def reset(self):
        pass


    def showBoard(self):
        for i in range(ROWS):
            print('--------------------')
            out = '| '
            for j in range(COLS):
                out += '0 | '  # Print '0' for all cels
            print(out)
        print('---------------------')


grid = Grid(state=(1,1))

if __name__ == "__main__":
    grid.showBoard()
