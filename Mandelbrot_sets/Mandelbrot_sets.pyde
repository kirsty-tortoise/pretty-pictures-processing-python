'''
The Mandelbrot set is made by investigating what happens starting with z = c under the iteration:
    z_(n+1) = z_n^2 + c
for varying values of c, where c is a complex number. 

These are then plotted on an Argand diagram if the sequence does not increase unboundedly. This makes a pretty picture.

You can also investigate similar sequences:
    z_(n+1) = z_n^3 + c
    z_(n+1) = z_n^4 + c
    z_(n+1) = z_n^5 + c
    etc.
    
These different sequences are changed by count, and you can get to the next one by clicking on the screen.
'''

from random import randrange
count = 2 # Mandelbrot number

def scale_num(num):
    # Take a coordinate number and convert to number in range -2 to 2
    return ((4.0 * num) / height) - 2

def general_test(c,n,number_of_iterations):
    """ This will test whether the complex number c is in the n th Mandelbrot set according to some number_of_iterations """
    z = c 
    for i in range(number_of_iterations):
        
        # Exclude zero to avoid division by zero.
        if n <= 0 and abs(z) == 0.0:
            return False
        
        z = z ** n + c
        if abs(z) > 2:
            return False
    else:
        # Not out of the range yet, so probably in the set.
        return True

def setup():
    # Set up screen
    size(800, 800)
    colorMode(HSB, 360, 100, 100) # Use HSB to make random colours easier.
    background(randrange(360), 20, 90)
    
def draw():
    # Carry out 500 iterations each loop.
    for i in range(500):
        newx = randrange(width)
        newy = randrange(height)
        # Test whether to plot it.
        if general_test(complex(scale_num(newx), -scale_num(newy)), count, 10):
            point(newx, newy)
            
def mousePressed():
    # When clicked, reset background and show next set.
    global count
    background(randrange(360), 20, 90)
    count += 1