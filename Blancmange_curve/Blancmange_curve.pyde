'''
The Blancmange Curve is defined by the equation:
    y = SUM s(2^n x) / 2^n
where s(x) is the distance between x and the nearest integer and x is between 0 and 1.
'''

def setup():
    global x
    size(800, 800)
    x = 0
    background(255)

def draw():
    # Plots a line from the x axis to the y coordinate determined 
    # by the function for the next x value
    global x
    if x <= 1:
        plot(x, blanc(x))
        x += 1.0 / width

def plot(a, b):
    # Draws a vertical line from the x axis to (a, b)
    stroke(255, 100, 100)
    line(a * width, height, a * width, (1 - b) * height)

def s(x):
    # returns the difference between x and the nearest integer
    return min(x - int(x), int(x + 1) - x)

def blanc(x):
    # Tests an x value to find the y value
    S = 0
    for i in range(20):
        S += s(2 ** i * x) / 2.0 ** i
    return S
