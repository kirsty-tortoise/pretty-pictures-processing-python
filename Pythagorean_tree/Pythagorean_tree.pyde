class Square:
    def __init__(self, mode, x, y, a, l):
        self.angle = a
        self.length = l
        if mode == "L":
            self.x1 = x + l * cos(radians(a + 90))
            self.y1 = y - l * sin(radians(a + 90))
            self.x2 = x + sqrt(2) * l * cos(radians(a + 45))
            self.y2 = y - sqrt(2) * l * sin(radians(a + 45))
            self.x3 = x +  l * cos(radians(a))
            self.y3 = y - l * sin(radians(a))
            self.x4 = x
            self.y4 = y
        if mode == "R":
            self.x2 = x + l * cos(radians(a + 90))
            self.y2 = y - l * sin(radians(a + 90))
            self.x1 = x + sqrt(2) * l * cos(radians(a + 135))
            self.y1 = y - sqrt(2) * l * sin(radians(a + 135))
            self.x3 = x
            self.y3 = y
            self.x4 = x +  l * cos(radians(180+a))
            self.y4 = y - l * sin(radians(180+a))
            
    def newleftsquare(self, a):
        return Square("L", self.x1, self.y1, self.angle + a, self.length * cos(radians(a)))
    
    def newrightsquare(self, a):
        return Square("R", self.x2, self.y2, self.angle + a - 90, self.length * sin(radians(a)))
    
    def draw_square(self):
        quad(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)

def setup():
    global squares, angle, c
    size(400, 400)
    angle = 39.0
    sidelength = 50.0
    squares = [Square("L", (width - sidelength) / 2.0, height - 10.0, 0, sidelength)]
    background(0)
    noStroke()
    c = 200
    fill(250, c, c)
    draw_all()

def draw():
    pass

def mouseClicked():
    global squares, c
    c *= 0.85
    fill(250, c, c)
    newsquares = []
    for i in squares:
        newsquares.append(i.newleftsquare(angle))
        newsquares.append(i.newrightsquare(angle))
    squares = newsquares
    draw_all()
    
def draw_all():
    for i in squares:
        i.draw_square()
