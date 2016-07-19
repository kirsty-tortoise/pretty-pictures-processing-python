n = 6
directions = [i * 360.0 / n for i in range(n)]
step = 10

def setup():
    global x, y
    size(400, 400)
    background(0)
    x = width / 2
    y = height / 2
    colorMode(HSB, 100)
    

def draw():
    global x, y
    angle = directions[int(random(n))]
    newx = x + step * sin(radians(angle))
    newy = y - step * cos(radians(angle))
    c = (frameCount * 0.1) % 100
    stroke(c, 100, 100)
    line(x, y, newx, newy)
    x, y = newx, newy

def mouseClicked():
    global x, y
    background(0)
    x = mouseX
    y = mouseY
