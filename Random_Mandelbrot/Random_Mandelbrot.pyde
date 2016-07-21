'''
This is mostly just a random walk, but the particle is confined to be inside the Mandelbrot set at all times. 
If you leave it running long enough, you can kind of see the Mandelbrot set, but coloured in randomly, which is a bit nice.

At every turn, the particle tries to take a small step in a randomly chosen direction. It checks if the new point would be inside the Mandelbrot set.
If the new point is not inside the Mandelbrot set, it chooses another direction and tries again without updating its position.
See the Mandelbrot set file for an explanation of the Mandelbrot set.

It takes a while to build up a reasonable picture because it is hard to get to some parts of the Mandelbrot set using this method.

Click to move on to a similar image of a Mandelbrot type set, but with iteration z_(n+1) = z_n^3+c etc.
'''

n = 2

def setup():
    global x, y, c, step
    # Set up screen
    size(400, 400)
    background(0)
    
    # Start at centre
    x = width / 2
    y = height / 2
    
    colorMode(HSB, 100) # Use HSB for smooth changing colours
    c = 0 # Starting colour is red
    stroke(c, 100, 100)
    
    step = 1

def draw():
    global x, y, c
    for i in range(100):
        A = True # Flags first loop
        while A or not general_test(3 * complex((newx / width - 1.0 / 2), (newy  / height - 1.0 / 2)), n, 50): # Scale in range -3/2 to 3/2 
            angle = random(360)
            newx = x + step * sin(radians(angle))
            newy = y - step * cos(radians(angle))
            A = False
        
        # Draw line from old point to new point once a suitable new point is found.
        line(x, y, newx, newy)
        x, y = newx, newy
        
        # Increase colour and wrap around.
        c = (c + 0.005) % 100
        stroke(c, 100, 100)

def mouseClicked():
    global x, y, c, n
    background(0)
    
    # Increase n and then reset everything
    n += 1
    x = width / 2
    y = height / 2
    c = 0
    stroke(c, 100, 100)
    
def general_test(c, n, number_of_iterations):
    """ This will test whether the complex number c is in the n th Mandelbrot set according to some number_of_iterations """
    z = c 
    for i in range(number_of_iterations):
        if n <= 0 and abs(z) == 0.0: # Avoid dividing by zero for negative n.
            return False
        z = z ** n + c
        if abs(z) > 2:
            return False
    else:
        # It hasn't escaped yet, so probably not in the Mandelbrot set.
        return True