'''
The Pythagorean tree is made up of squares and right angled triangles, although the right angled triangles are more "absense of squares".

The tree starts with one square. On every iteration, all of the active squares - the most recently added layer to the tree - produces two more new squares.
The top of the old square and the base of the two new squares makes a right angled triangle, with an angle that you can change to get a slightly different picture.
The classical angle is 45 degrees, but other angles look nice too - you can change this.

When running the program, click for the next iteration.
'''


class Square:
    def __init__(self, mode, x, y, a, l):
        self.angle = a
        self.length = l
        
        # To initiate a square, give angle of tilt and either
        # mode == L and coordinate of bottom coordinate and angle measured from horizontal clockwise for the square on the left side.
        # mode == R and coordinate of bottom coordinate and angle measured from horizontal anticlockwise for the square on the right side.
        if mode == "L":
            self.x1 = x + l * cos(radians(a + 90))
            self.y1 = y - l * sin(radians(a + 90))
            self.x2 = x + sqrt(2) * l * cos(radians(a + 45))
            self.y2 = y - sqrt(2) * l * sin(radians(a + 45))
            self.x3 = x +  l * cos(radians(a))
            self.y3 = y - l * sin(radians(a))
            self.x4 = x
            self.y4 = y
        elif mode == "R":
            self.x2 = x + l * cos(radians(a + 90))
            self.y2 = y - l * sin(radians(a + 90))
            self.x1 = x + sqrt(2) * l * cos(radians(a + 135))
            self.y1 = y - sqrt(2) * l * sin(radians(a + 135))
            self.x3 = x
            self.y3 = y
            self.x4 = x +  l * cos(radians(180+a))
            self.y4 = y - l * sin(radians(180+a))
            
    def newleftsquare(self, a):
        # Make a new left square with angle increased by a
        return Square("L", self.x1, self.y1, self.angle + a, self.length * cos(radians(a)))
    
    def newrightsquare(self, a):
        # Make a new right square with angle decreased by 90 - a (as the other two angles in triangle add to 90).
        return Square("R", self.x2, self.y2, self.angle + a - 90, self.length * sin(radians(a)))
    
    def draw_square(self):
        quad(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3, self.x4, self.y4)

def setup():
    global squares, angle, c
    size(400, 400)
    background(0)
    noStroke()
    
    # You can change these!
    angle = 39.0 # in degrees
    sidelength = 50.0
    
    # Start with one square at the bottom
    squares = [Square("L", (width - sidelength) / 2.0, height - 10.0, 0, sidelength)]
    
    # Draw in various shades of red by changing the amount of blue and green.
    c = 200
    fill(250, c, c)
    
    draw_all()

def draw():
    pass

def mouseClicked():
    global squares, c
    
    c *= 0.85 # Decreases green and blue to make red brighter
    fill(250, c, c)
    
    # Change squares to be the new ACTIVE / top level squares
    newsquares = []
    for i in squares:
        newsquares.append(i.newleftsquare(angle))
        newsquares.append(i.newrightsquare(angle))
    squares = newsquares
    
    # Display the new squares
    draw_all()
    
def draw_all():
    for i in squares:
        i.draw_square()