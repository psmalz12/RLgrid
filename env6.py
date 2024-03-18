
ROWS = 5
COLS = 5
Win_State = (1, 5) # i did not use it yet
# Lose_State= (2, 4) can def this later as loss -1 for RL learning


class Grid:
    def __init__(self, state):
        self.state = state
        self.board = []
        for _ in range(ROWS + 2):
            row= [] # creat a list for each rows to appand a value later
            for _ in range(COLS + 2):
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


grid = Grid(state=(1,1)) # intit with the start state

if __name__ == "__main__":
    grid.showBoard()
