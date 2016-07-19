def setup():
    global stage, n
    size(1000, 1000)
    background(0)
    stroke(255)
    stage = "F"
    n = 0

def Lprocess(seq, angle, n):
    a = 0
    step = 600.0 / (3 ** n)
    x = width/2 - 250
    y = height/2 + 250
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
        num = random(1)
        if k == "F":
            if num >= 0.5:
                new += "F-F++F-F"
            else:
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
