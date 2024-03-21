import random

ROWS = 7
COLS = 7
Goal = (1, 5)
walls = [(2,5),(2,4),(2,3), (3,2)]

# solved the move agent fun it was an axis issue 20/03/2024

class Grid:
    def __init__(self, state):
        self.state = state
        self.board = []
        self.num_iter = 0 # to print later the num of iter in action fun
        self.cur_action_state_pair = []  # tuple list to save state-action pairs for the current iteration



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



    def action(self, num_iter):
        self.num_iter = num_iter  # update the num iter
        directions = ["left", "right", "up", "down"]
        action_state_pair = []  # initialize the list to store action-state pairs
        for _ in range(num_iter):
            random_direction = random.choice(directions)
            print(f"Next Move: {random_direction}")
            new_state = self.agentmove(random_direction)  # get the new state after the action
            if random_direction == "up":
                action_code = 1
            elif random_direction == "down":
                action_code = 2
            elif random_direction == "right":
                action_code = 3
            elif random_direction == "left":
                action_code = 4
            self.cur_action_state_pair.append((self.flatten_state(new_state), action_code))
            action_state_pair.append(( self.flatten_state(new_state), action_code))
            self.showBoard()
            print("State', Action:", self.cur_action_state_pair)
            self.cur_action_state_pair = []  # Reset current iteration pairs

            #print(f"State', Action: {action_state_pair}") # this if i want to see all the pairs in that iter

        print(f'Number of Iterations: {self.num_iter}')
        return action_state_pair


    def agentmove(self, dest):
        # current position of the agent
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
            # invalid direction the agent stay in the same position
            fcol = x
            frow = y

        # Check if the new position is valid (not a wall and within the grid)
        if self.board[fcol][frow] != 1:
            # Update the state of the agent
            self.state = (fcol, frow)
            print(f'//////// agent New Location : {self.state} ////////')
            fla_state = self.flatten_state(self.state)  # Convert (x, y) to flattened state
            print(f'Flattened State: {fla_state}')



        else:
            print('Faced an Obstacle or a Wall')
            print(f'//////// agent Stay at Location : {self.state} ////////')



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

    def flatten_state(self, state):
        x, y = state
        return x * COLS + y

    #fla_state = self.flatten_state(self.state)  # Convert (x, y) to flattened state

    def get_coord(self):
        x = self.state // COLS
        y = self.state % COLS
        return x, y
    #cord_state = self.flatten_state(self.state)  # Convert (x, y) to flattened state



if __name__ == "__main__":
        grid = Grid(state=(5, 1))
        print('//////// agent current Location "2" ////////')
        grid.showBoard()
        grid.action(10)



# this hiw i imagin the grid
#[0][0] [0][1] [0][2] [0][3] [0][4] [0][5] [0][6]
#[1][0] [1][1] [1][2] [1][3] [1][4] [1][5] [1][6]
#[2][0] [2][1] [2][2] [2][3] [2][4] [2][5] [2][6]
#[3][0] [3][1] [3][2] [3][3] [3][4] [3][5] [3][6]
#[4][0] [4][1] [4][2] [4][3] [4][4] [4][5] [4][6]
#[5][0] [5][1] [5][2] [5][3] [5][4] [5][5] [5][6]
#[6][0] [6][1] [6][2] [6][3] [6][4] [6][5] [6][6]
