import tkinter as tk   # just to creat a graphical interface
# https://python-course.eu/tkinter/canvas-widgets-in-tkinter.php
# https://javatpoint.com/python-tkinter-canvas

class Grid:
    def __init__(self):
        self.gr = tk.Tk()
        self.frame = tk.Canvas(self.gr, bg='grey', height=500, width=500)
        self.gr.title("Grid World 5 x 5")
        self.frame.pack(padx=20, pady=20)  # padx to control the position horizontal and pady vertical
        self.grid()  # initialize the grid environment
        self.gr.mainloop()  # Start the Tkinter main loop


# x ----> blue //// y ----> green
    def draw(self): # is not showing anything
        # draw x-axis (start from 0 in x, start horizon position 500, end in 500 in x, end in horizon position in 500)
        self.frame.create_line(0, 500, 500, 500, fill='light blue', width=5)

        # draw y-axis (start virtical position 2, start from 0 in y, end in virtical position in 2,  end in 500 in y)
        self.frame.create_line(2, 0, 2, 500, fill='light green', width=5)
        # draw gool cel (0,4) ( end from horizon 500, end virtical in 100, start from horizon 400, start virtical in 0)
        self.frame.create_rectangle(500, 100, 400, 0, fill='green') # the gool cel


    def grid(self):
        gool_cells = [ (0,4) ]
        black_cells = [(3, 1), (2, 1) , (1, 2) , (1,3) , (1,4)]# Define coordinates of black cells
        #  grid world environment
        for i in range(5): # row H
            for j in range(5):  # col W
                if (i, j) not in black_cells:  # Check if cell is not black
                    x1, y1 = j * 100, i * 100  # j * 100  horizen line of the cel and i*100 virtical
                    x2, y2 = x1 + 100, y1 + 100
                    self.frame.create_rectangle(x1, y1, x2, y2, fill='white')

        # call draw fun because we will draw the grid here
        self.draw()

        # start position of the agent
        agent_x = 50  # x-coordinate of the agent
        agent_y = 450  # y-coordinate of the agent
        self.agent = self.frame.create_oval(agent_x - 20, agent_y - 20, agent_x + 20, agent_y + 20, fill='blue') # chape and color

    def move_agent(self):
        # need to adjest as i need in the env
        if move == 'up':
            # conditions for moving up
            pass
        elif move == 'right':
            pass
        elif move == 'left':
            pass
        elif move == 'down':
            pass


        self.frame.update()





# Create an instance of the GridWorld class and display the grid world with the agent
grid_world = Grid()
