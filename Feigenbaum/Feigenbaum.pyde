'''
This image is made by investigating the iterative sequence:
    new_a = r old_a (1-old_a)
for different values of r.

Values of r are on the horizontal axis and the value(s) of a that the sequence tends to in the long run are on the vertical axis.
'''

def setup():
    # Sets up canvas, colours and backgrounds
    colorMode(HSB, 100)
    size(800, 800)
    background(20, 60, 100)
    stroke(0)
    
    # Frame rate is increased so it draws more quickly
    frameRate(200)
    
    # r is the current value being investigated
    global r
    r = 2

def draw():
    # Look at the next value of r, check and plot it, and then increase r
    global r
    check_number()
    r += 2.0 / width 

def check_number():
    # Investigate what happens to the iteration new_a = r old_a (1-old_a)
    # First a is always 0.5
    a = 0.5
    
    # Some initial points should be discounted as anomalies
    for i in range(100):
        a = r * a * (1 - a)
        
    # Plots all of the next points at the x coordinate corresponding to r and y coordinate corresponding to a
    for i in range(200):
        a = r * a * (1 - a)
        point(width * (r - 2) / 2.0, (1 - a) * height)
