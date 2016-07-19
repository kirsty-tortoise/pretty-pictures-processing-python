

def setup():
    global stage, n
    size(1000, 1000)
    background(0)
    stroke(300, 0, 0)
    stage = "F++F++F"
    n = 0

def Lprocess(seq, angle, n):
    a = 0
    step = 300.0 / (3 ** n)
    x = width/2 - 250
    y = height/2
    for j in seq:
        if j == "F":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        elif j == "+":
            a += angle
        elif j == "-":
            a -= angle
    x = width/2 - 250 + 300
    y = height/2
    for j in seq:
        if j == "F":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        elif j == "+":
            a += angle
        elif j == "-":
            a -= angle
    a = -120
    x = width/2 - 250
    y = height/2
    for j in seq:
        if j == "F":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        elif j == "+":
            a += angle
        elif j == "-":
            a -= angle

def nextstage(stage):
    new = ""
    for k in stage:
        if k == "F":
            new += "F+F--F+F"
        else:
            new += k
    return new

def draw():
    pass

def mousePressed():
    global stage, n
    stage = nextstage(stage)
    n += 1
    background(0)
    Lprocess(stage, 60, n)
    
