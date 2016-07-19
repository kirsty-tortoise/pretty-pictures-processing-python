from random import randrange
COUNT = 2

def scale_num(num):
    return ((4.0 * num) / height) - 2

def general_test(c,n,number_of_iterations):
    """ This will test whether the complex number c is in the n th Mandelbrot set according to some number_of_iterations """
    z = c 
    for i in range(number_of_iterations):
        if n <= 0 and abs(z) == 0.0:
            return False
        z = z ** n + c
        if abs(z) > 2:
            return False
    else:
        return True

def setup():
    size(800, 800)
    colorMode(HSB, 360, 100, 100)
    background(randrange(360), 20, 90)
    
def draw():
    for i in range(500):
        newx = randrange(width)
        newy = randrange(height)
        if general_test(complex(scale_num(newx), -scale_num(newy)), COUNT, 10):
            point(newx, newy)
            
def mousePressed():
    global COUNT
    background(randrange(360), 20, 90)
    COUNT += 1
