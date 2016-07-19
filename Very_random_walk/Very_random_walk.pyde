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
        angle = random(360)
        newx = x + step * sin(radians(angle))
        newy = y - step * cos(radians(angle))
        line(x, y, newx, newy)
        x, y = newx, newy
        c = (c + 0.01) % 100
        stroke(c, 100, 100)

def mouseClicked():
    global x, y, c
    background(0)
    x = mouseX
    y = mouseY
    c = 0
    stroke(c, 100, 100)
