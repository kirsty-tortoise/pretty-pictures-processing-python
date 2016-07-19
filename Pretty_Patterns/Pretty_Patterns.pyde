def hexagon(centreX, centreY, radius):
    beginShape()
    for j in range(0, 360, 60):
        vertex(centreX + radius * cos(radians(j)), centreY + radius * sin(radians(j)))
    endShape(CLOSE)

def drawhexagons(radius):
    indent = 0
    for i in range(width / 8 , width - width / 8, radius):
        indent = not indent
        for j in range(height / 8, height - height / 8, int(2 * sqrt(3) * radius)):
            if random(1) > 0.35:
                fill(random(100), 50, 80, 40)
                for count in range(6):
                    hexagon(j + radius * sqrt(3) * indent, i, radius)
                    translate(width / 2, height / 2)
                    rotate(PI/3.0)
                    translate(- width / 2,- height / 2)
                    
def drawrandomhexagons(radius):
    for x in range(40):
        i = random(0, width)
        j = random(0, height)
        fill(random(100), 50, 80, 50)
        for count in range(6):
                hexagon(i, j, radius)
                translate(width / 2, height / 2)
                rotate(PI/3.0)
                translate(- width / 2,- height / 2)

def setup():
    size(800, 800)
    noStroke()
    background(0)
    colorMode(HSB, 100)
    drawrandomhexagons(40)
    
def draw():
    pass
    
def keyPressed():
    background(0)
    if key == "a":
        drawhexagons(40)
    elif key == "b":
        drawrandomhexagons(40)
    
