'''
In a random walk, you start at a point, and then make steps in a random direction, moving around the screen, and the motion is tracked.
The colour changes too, making a pretty picture.

In this random walk, the steps are quite large and a fixed number of directions are chosen (controlled by n). 
Fewer directions means less space can be explored and the picture looks more controlled, more directions mean the picture looks more random.

When running the program, click to clear the screen and start the random walk again, from the point you clicked.
'''

n = 6
directions = [i * 360.0 / n for i in range(n)]
step = 10

def setup():
    global x, y
    size(400, 400)
    background(0)
    
    # Start in the centre of the screen.
    x = width / 2
    y = height / 2
    
    colorMode(HSB, 100) # Allow cycling through colours easily.
    

def draw():
    global x, y
    angle = directions[int(random(n))]
    newx = x + step * sin(radians(angle))
    newy = y - step * cos(radians(angle)) # - because decreasing y is upwards in Processing.
    
    # Decide the colour based on the frameCount.
    c = (frameCount * 0.1) % 100
    stroke(c, 100, 100)
    
    # Draw the line, then update.
    line(x, y, newx, newy)
    x, y = newx, newy

def mouseClicked():
    global x, y
    background(0)
    x = mouseX
    y = mouseY