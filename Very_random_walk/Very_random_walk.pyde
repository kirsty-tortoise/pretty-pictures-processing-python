'''
In a random walk, you start at a point, and then make steps in a random direction, moving around the screen, and the motion is tracked.
The colour changes too, making a pretty picture.

In this random walk, the steps are very small and the direction chosen is a random number of degrees, chosen uniformly from 0 to 360. This makes it look quite random.

When running the program, click to clear the screen and start the random walk again, from the point you clicked.
'''


def setup():
    global x, y, c, step
    size(400, 400)
    background(0)
    
    # Start in the centre of the screen.
    x = width / 2
    y = height / 2
    
    colorMode(HSB, 100) # Use HSB to change colour smoothly
    c = 0 # Start with a red colour
    stroke(c, 100, 100)
    
    step = 1

def draw():
    global x, y, c
    for i in range(100): # Move 100 steps per frame.
        angle = random(360)
        newx = x + step * sin(radians(angle))
        newy = y - step * cos(radians(angle)) # Decreasing y means moving up the screen, hence the minus.
        line(x, y, newx, newy)
        x, y = newx, newy
        
        # Increase colour, wrapping back around at 100
        c = (c + 0.01) % 100
        stroke(c, 100, 100)

def mouseClicked():
    global x, y, c
    background(0)
    x = mouseX
    y = mouseY
    c = 0
    stroke(c, 100, 100)