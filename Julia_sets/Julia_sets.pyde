'''
The Julia sets are based on investigating the following iterative sequence:
    newZ = oldZ^2 + c
for varying complex starting points z, for some fixed c.

If this sequence does not ever go towards infinity, then that starting value of z is considered to be in that Julia set.

To get an image, plot all the points in that Julia set on the complex plane.
'''


from random import randrange

# pretty_sets is a preset list of some complex numbers with nice Julia sets
pretty_sets = [complex(-0.123, 0.745), complex(-0.62772, 0.42193), complex(0.3515, -0.07467), complex(-0.74434, -0.10772)]
# count is the pretty set index that is now being displayed, c is that complex number
count = 0
c = pretty_sets[count]

def scale_num(num):
    # scales an x or y coordinate in the maths to an x or y coordinate on the screen
    return ((4.0 * num) / height) - 2

def julia_test(startz, number_of_iterations):
    # This will test whether the complex number c is in the n th Mandelbrot set according to some number_of_iterations
    z = startz
    n = 2
    
    # Iterate number_of_iterations times and see if the values get bigger than 2
    for i in range(number_of_iterations):
        if n <= 0 and abs(z) == 0.0:
            return False
        z = z ** n + c
        if abs(z) > 2:
            return False
    else:
        return True

def setup():
    # Sets up canvas, colours and background
    size(800, 800)
    colorMode(HSB, 360, 100, 100) # HSB so nice random colours can be chosen
    background(randrange(360), 20, 90) # Nice pastel background
    
def draw():
    # Choose and test 500 numbers each frame
    for i in range(500):
        # Choose a random x and y coordinate on the screen
        newx = randrange(width)
        newy = randrange(height)
        
        # Plot the point if it is part of this Julia set
        if julia_test(complex(scale_num(newx), - scale_num(newy)), 40):
            point(newx, newy)

def mousePressed():
    # When the mouse is pressed, move to the next set
    global c, count
    background(randrange(360), 20, 90)
    count = (count + 1) % len(pretty_sets)
    c = pretty_sets[count]
