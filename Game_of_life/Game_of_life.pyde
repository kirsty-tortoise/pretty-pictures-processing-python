'''
Game of life is a simulation based on a grid of cells, which are all either alive or dead.

To get from one iteration to the next, the following rules are used:
    -> If a cell is currently alive then it needs two or three neighbours to survive, else it dies from overcrowding or underpopulation
    -> If a cell is currently dead, it needs exactly three neighbours for reproduction to occur and it to come alive
    
This is carried out many times from some starting grid to create pretty pictures.
'''

bottom = 100 # sets how high the bottom of the grid is

def setup():
    size(600, 600 + bottom)
    
    # Too many global variables - this would really benefit from classes?    
    # Set up colours, and then switch to HSB
    global white, black, grey
    white = color(255)
    black = color(0)
    grey = color(200)
    colorMode(HSB, 100)

    # n is the size of the grid, and the grid stores the current state
    global n, grid
    n = 5
    grid = make_grid(n)
    # Then draw the grid
    draw_grid()
    
    # Now draw the bottom panel
    noStroke()
    fill(70, 50, 80)
    rect(0, width, width, bottom)
    
    # startw and starth represent the width/height of the start button
    # startx and starty represent its x and y coordinates
    # Then actually draw the button
    global startw, starth, startx, starty
    startw = width / 3
    starth = bottom * 0.8
    startx = width / 4
    starty = height - bottom / 2
    draw_start()
    
    draw_plus_minus_buttons()
    
    # At the start, you aren't playing
    global Playing
    Playing = False
    
    # time and wait are used to control the speed of the iteration
    global time, wait
    time = millis()
    wait = 200
    
def update(grid):
    # Takes a grid and returns what it looks like after one iteration
    
    # Make a new empty grid with all dead cells
    newgrid = make_grid(n)
    
    for i in range(n):
        # a and b are the y coordinate limits around the cell i,j you are looking at
        a = max(0, i - 1)
        b = min(n, i + 2)
        
        for j in range(n):
            # c and d are the x coordinate limits around the cell i,j you are looking at
            c = max(0, j - 1)
            d = min(n, j + 2)
            
            # Find the neighbours (including itself) by summing the values for its neighbours in the existing grid
            neighbours = sum([sum([grid[y][x] for y in range(a, b)]) for x in range(c, d)])
            
            # If the cell is alive, it survives if it has 3 or 4 neighbours (including itself)
            if grid[i][j]:
                if neighbours in [3, 4]:
                    newgrid[i][j] = 1 

            # If the cell is not alive, it needs precisely 3 neighbours to come to life
            else:
                if neighbours == 3:
                    newgrid[i][j] = 1
                    
    return newgrid

def draw_plus_minus_buttons():
    # Sets up settings for drawing all the buttons and adds text explaining what they do
    noStroke()
    rectMode(CENTER)
    textAlign(CENTER, TOP)
    textSize(0.2 * bottom)
    text("Number of cells", 3 * width / 4, height - 5 * bottom / 6, width / 2, bottom / 3)
    textSize(0.4 * bottom)
    
    global minusx, plusx, pmy, pmh, pmw
    pmh, pmw = min(bottom / 2, 3 * width / 32.0), min(bottom / 2, 3 * width / 32.0)
    minusx = 11 * width / 16
    plusx = 13 * width / 16
    pmy = height - 2 * bottom / 5
    
    # Draws the minus button in red
    fill(0, 80, 80)
    rect(minusx, pmy, pmw, pmh, 10)
    fill(0)
    text("-", minusx, pmy, pmw, pmh)
    
    # Draws the plus button in green
    fill(20, 80, 80)
    rect(plusx, pmy, pmw, pmh, 10)
    fill(0)
    text("+", plusx, pmy, pmw, pmh)
    rectMode(CORNER)

def draw_start():
    # Draws the start button in green
    noStroke()
    fill(20, 80, 80)
    rectMode(CENTER)
    rect(startx, starty, startw, starth, 10)
    
    # Adds text saying "START"
    fill(0)
    textSize(0.38 * bottom)
    textAlign(CENTER, CENTER)
    text("START", startx, starty, startw, starth)
    rectMode(CORNER)

def draw_stop():
    # Draws the stop button in red
    noStroke()
    fill(0, 80, 80)
    rectMode(CENTER)
    rect(startx, starty, startw, starth, 10)
    
    # Adds text saying "STOP"
    fill(0)
    textSize(0.38 * bottom)
    textAlign(CENTER, CENTER)
    text("STOP", startx, starty, startw, starth)
    rectMode(CORNER)

def make_grid(n):
    # Creates an empty n by n grid
    return [[0 for i in range(n)] for j in range(n)]

def draw_grid():
    # Draws the grid to the screen
    stroke(0)
    for i in range(n):
        for j in range(n):
            # Alive cells are black, dead cells are white
            if grid[i][j]:
                fill(black)
            else:
                fill(white)
            # Draw a rectangle the correct place to screen coordinates
            rect((width * j) / float(n), ((height - bottom) * i) / float(n), width / float(n), (height - bottom) / float(n))

def draw():
    # If there has been a long enough pause since the last iteration, update the grid, redraw and reset the time
    global grid, time
    if Playing and millis() - time >= wait:
        grid = update(grid)
        draw_grid()
        time = millis()

def mousePressed():
    global Playing, n
    
    # If the square clicked is in the grid, change that square and redraw the grid
    if height - mouseY > bottom:
        global grid
        grid[int(mouseY * n / width)][int(mouseX * n / width)] ^= 1
        draw_grid()
    
    # If they click the start/stop button, change playing and update the button
    elif isOver(startx, starty, startw, starth):
        if Playing:
            Playing = False
            draw_start()
        else:
            Playing = True
            draw_stop()
    
    # If they click the plus button, add a square and refresh the grid
    elif isOver(plusx, pmy, pmw, pmh):
        n += 1
        grid = make_grid(n)
        draw_grid()
        
    # If they click the minus button, take away a square and refresh the grid
    elif isOver(minusx, pmy, pmw, pmh):
        if n > 1:
            n -= 1
            grid = make_grid(n)
            draw_grid()
    
def isOver(x, y, w, h):
    # Is the mouse over the button with coordinates (x,y), width w and height h?
    return x - w/2 <= mouseX <= x + w/2 and y - h/2 <= mouseY <= y + h/2