'''
The chaos game fern is created by starting at (0, 0) and following one of four
rules to transform the point with different probabilities. This is repeated and
all these points are plotted. 

The rules are:
    Rule 1 [0.01 probability]: (x, y) -> (0, 0.16y)
    Rule 2 [0.07 probability]: (x, y) -> (0.2x-0.26y, 0.23x+0.22y+1.6)
    Rule 3 [0.07 probability]: (x, y) -> (-0.15x+0.28y, 0.26x+0.24y+0.44)
    Rule 4 [0.85 probability]: (x, y) -> (0.85x+0.06y, -0.06x+0.85y+1.6)
'''

def setup():
    # Sets up canvas, background and colour
    size(800, 800)
    colorMode(RGB, 100)
    background(0)
    stroke(0, 100, 0)

    
def plot(x, y):
    # Draws a point at (x, y) in some coordinate system to the canvas scaled correctly
    point(width / 2.0  + x * width/10.0, height - y * height /12.0)
    
x = 0
y = 0

def transform(x, y):
    # Chooses a random number to decide what rule to apply
    num = random(1)
    if num <= 0.01:
        # Rule 1: (x, y) -> (0, 0.16y)
        newx = 0
        newy = 0.16 * y
    elif num <= 0.08:
        # Rule 2: (x, y) -> (0.2x-0.26y, 0.23x+0.22y+1.6)
        newx = 0.2 * x - 0.26 * y
        newy = 0.23 * x + 0.22 * y + 1.6
    elif num <= 0.15:
        # Rule 3: (x, y) -> (-0.15x+0.28y, 0.26x+0.24y+0.44)
        newx = -0.15 * x + 0.28 * y
        newy = 0.26 * x + 0.24 * y + 0.44
    else:
        # Rule 4: (x, y) -> (0.85x+0.06y, -0.06x+0.85y+1.6)
        newx = 0.85 * x + 0.06 * y
        newy = -0.06 * x + 0.85 * y + 1.6
    return (newx, newy)

def draw():
    # Each frame, carry out the iteration 100 times
    global x, y
    for i in range(100):
        x, y = transform(x, y)
        plot(x, y)
