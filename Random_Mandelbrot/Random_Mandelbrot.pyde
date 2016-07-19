n = 2

def setup():
    global x, y, c, step
    size(400, 400)
    background(0)
    x = width / 2
    y = height / 2
    colorMode(HSB, 100)
    c = 0
    stroke(c, 100, 100)
    step = 1

def draw():
    global x, y, c
    for i in range(100):
        A = True
        while A or not general_test(3 * complex((newx - width / 2), (newy - height / 2))/ height, n, 50):
            angle = random(360)
            newx = x + step * sin(radians(angle))
            newy = y - step * cos(radians(angle))
            A = False
        line(x, y, newx, newy)
        x, y = newx, newy
        c = (c + 0.005) % 100
        stroke(c, 100, 100)

def mouseClicked():
    global x, y, c, n
    background(0)
    n += 1
    x = width / 2
    y = height / 2
    c = 0
    stroke(c, 100, 100)
    
def general_test(c, n, number_of_iterations):
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
