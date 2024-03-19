# this code updated 19/03/2024 to add empty, goal spaces at the arrey than show the location of the agent by '2'

ROWS = 5
COLS = 5
Goal = (1,5)
walls = [(2,5),(2,4),(2,3), (3,2)]



class Grid:
    def __init__(self,state): # init the grid with one arg that the agent ini state where
        self.state = state
        self.board =[] # 2D list serve as an array for the grid

        for x in range(ROWS +2):
            row= [] # creat a list for each rows to appand a value later
            for y in range(COLS +2):
                if (x,y) == Goal:
                    row.append('G')
                elif (x,y) in walls:
                    row.append(1)
                else:
                    row.append(0)  # now appand the 0 to the empty list of row for each cell
            self.board.append(row)

        # fill border columns "x&y" with $ to drow invesble border of the grid world (5x5)
        # i can use this later to tell the agent if he obserave $ that mean he can not move toward that sign because it is borfer
        for x in range(ROWS +2):
            self.board[x][0] = self.board[x][COLS + 1] = '$'
        for y in range(COLS +2):
            self.board[0][y] = self.board[ROWS + 1][y] = '$'


    def agentmove(self):
        pass

    def reset(self):
        pass # what this will effect state value?


    def showBoard(self):
        for x in range(ROWS):
            print('----------------------')
            out = '| '
            for y in range(COLS):
                if (x +1, y+ 1) == self.state: # the agent still not moving so i put it in state (5,1) where is it in the buttom left
                    out += '2 | '  #  '2' for the robot's location
                elif (x +1, y+ 1) == Goal:
                    out += 'G | '  #  'G' for the goal state
                elif self.board[x+ 1][y+ 1] == 1:
                    out += '# | '  # check the tuple value in board if it = 1 than drow # for walls
                elif self.board [x+ 1][y+ 1] == 0:
                    out += '  | '  #  check the value in board if it = 0 than do a 'space' for empty cells
            print(out)
        print('---------------------')


grid = Grid(state=(5,1))

if __name__ == "__main__":
    grid.showBoard()
