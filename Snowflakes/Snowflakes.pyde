def snowflakes(x, y, flakeLength, flakes = 5, numberOfPoints = 5):
    lastFlake = []
    l = flakeLength / float(numberOfPoints)
    angled = TWO_PI / flakes
    
    for p in range(1, numberOfPoints + 1):
        lastFlake.append((x + p * l, y))
        
    for a in range(0, flakes + 1):
        newFlake = []
        angle = a * angled
        for p in range(1, numberOfPoints + 1):
            newFlake.append((x + p * l * cos(angle), y - p * l * sin(angle)))
            line(newFlake[-1][0], newFlake[-1][1], lastFlake[-p][0], lastFlake[-p][1])
        line(x, y, x + cos(angle) * flakeLength, y - sin(angle) * flakeLength)
        lastFlake = newFlake

def tileSnowflakes():
    background(0)
    colorMode(HSB, 360, 360, 360)
    jump = 0
    for count1 in range(10):
        for count2 in range(12):
            stroke(random(360), 300, 300)
            snowflakes((count1 + 0.5) * width / 10 + jump, (count2 + 0.5) * width * sqrt(3) / 20, 48, 6, 6)
            if jump == 0:
                jump = width / 20.0
            else:
                jump = 0

def setup():
    size(1000, 1000)
    tileSnowflakes()


def draw():
    pass

def keyPressed():
    tileSnowflakes()
