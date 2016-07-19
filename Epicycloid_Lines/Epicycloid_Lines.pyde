'''
A point is chosen on a unit circle, and the angle between this point and the x 
axis is multiplied by the factor to give a new point. These points are connected, 
and then the angle is multiplied by the factor again, and this is repeated.

The envelope of all these lines forms an epicycloid, depending on the value of factor.
'''

# factor is the number the angle is multiplied by each iteration
factor = 2
# angle is the starting angle, in radians
angle = 1
black = color(0)

def setup():
    # Sets up the canvas and background. Colour is set randomly.
    size(400, 400)
    background(black)
    colorMode(HSB, 100)
    stroke(random(100), 80, 100)
    
    # x and y are set to their starting values
    global x, y
    x, y = f(angle)
    
def draw():
    # Update the angle by multiplying by factor modulo Tau, so the numbers don't get big.
    global angle, x, y
    angle = (angle * factor) % TAU
    newx, newy = f(angle)
    # Plot a line from the old point to the new point
    line(x, y, newx, newy)
    # Update x and y
    x, y = newx, newy

def f(angle):
    # Translates an angle into a set of coordinates for the screen
    x = width / 2 + width / 3 * cos(angle)
    y = height / 2 - height / 3 * sin(angle)
    return (x, y)

def mouseClicked():
    # When clicked, increase the factor, reset the screen and choose a new colour
    global factor
    background(black)
    stroke(random(100), 80, 100)
    factor += 1
