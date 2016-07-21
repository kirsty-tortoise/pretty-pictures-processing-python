'''
Penrose tilings are non-periodic tilings, so they don't repeat, even though they tesselate exactly. 
In this case the tilings are "kites" and "darts", but these are actually made of two triangles each (red and blue respectively)

One way to generate these rules is by a substitution rule, where you replace one triangle with two or three others. 
There is a different but consistent rule for red and blue triangles.

Phi, the golden ratio, is important here, as it happens to give the right ratio for the triangles. The angles 36 and 72 degrees are also useful here. 
This is because all things here are quite pentagon-ish.
'''

# The golden ratio, solution to x^2 = x + 1, and the constant that makes things work.
PHI = (1 + sqrt(5)) / 2.0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # For some reason I defined multiplying as splitting in ratio PHI : PHI - 1
    def __mul__(A, B):
        return Point(A.x + (PHI - 1) * (B.x - A.x), A.y + (PHI - 1) * (B.y - A.y))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        
    def draw_edges(self):
        # Only two of the edges are drawn, as triangles are only half darts / kites
        stroke(0)
        line(self.p2.x, self.p2.y, self.p3.x, self.p3.y)
        line(self.p1.x, self.p1.y, self.p3.x, self.p3.y)

class Type1(Triangle):
    
    # Red triangles for kites
    
    def draw_triangle(self):
        noStroke()
        fill(255, 0, 0)
        triangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)
    
    def split_triangle(self):
        # Split a red triangle into two red triangles and a blue triangle.
        new1 = self.p1 * self.p2
        new2 = self.p3 * self.p1
        t1 = Type1(self.p3, new1, new2)
        t2 = Type1(self.p3, new1, self.p2)
        t3 = Type2(new2, self.p1, new1)
        return [t1, t2, t3]

class Type2(Triangle):
    
    # Blue triangles for darts
    
    def draw_triangle(self):
        noStroke()
        fill(0, 0, 255)
        triangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)
    
    def split_triangle(self):
        # Split a blue triangle into one red and one blue triangle.
        new = self.p2 * self.p3
        t1 = Type1(self.p2, self.p1, new)
        t2 = Type2(new, self.p3, self.p1)
        return [t1, t2]

def setup():
    global triangles
    size(800, 800)
    triangles = half_kite() # Change this strategy to draw slightly different pictures.
    draw_all(triangles) # Draw them the first time. 

def draw():
    pass

def mouseClicked():
    global triangles
    triangles = update_all(triangles)
    draw_all(triangles)

def draw_all(triangles):
    # Reset everything by flooding the background.
    background(255)
    
    for i in triangles:
        i.draw_triangle()
    for i in triangles:
        i.draw_edges()

def update_all(triangles):
    # Split all the triangles into the new list.
    newtriangles = []
    for i in triangles:
        newtriangles += i.split_triangle()
    return newtriangles

def half_kite():
    # Sets up a half_kite arrangement (a red triangle) to start with. 
    l = 2/3.0 * width
    bottom = height / 4.0
    p1 = Point(1/6.0 * width, height - bottom)
    p2 = Point(5/6.0 * width, height - bottom)
    p3 = Point(1/6.0 * width + cos(radians(36)) * l, height - bottom - l * sin(radians(36)))
    return [Type1(p1, p2, p3)]

def half_dart():
    # Sets up a half_dart arrangement (a blue triangle) to start with.
    l = 2/3.0 * width
    bottom = height / 2.5
    p1 = Point(width / 2.0, height - bottom - l * tan(radians(36))/2.0) 
    p2 = Point(1/6.0 * width, height - bottom)
    p3 = Point(5/6.0 * width, height - bottom)
    return [Type2(p1, p2, p3)]
    
def sun():
    # Sets up a sun / circular arrangement to start with.
    tri = []
    l = 1/3.0 * width
    c = Point(width / 2.0, height / 2.0)
    angle = 0
    
    # Add 10 triangles in a circle using a loop - one red, one blue per iterations
    for i in range(5):
        p1 = Point(width / 2.0 + l * cos(angle), height / 2.0 - l * sin(angle))
        angle += PI / 5.0
        p2 = Point(width / 2.0 + l * cos(angle), height / 2.0 - l * sin(angle))
        angle += PI / 5.0
        p3 = Point(width / 2.0 + l * cos(angle), height / 2.0 - l * sin(angle))
        tri.append(Type1(c, p2, p1))
        tri.append(Type1(c, p2, p3))
    
    return tri

def star():
    # Sets up a star arrangement to start with.
    tri = []
    l2 = 1/4.0 * width
    l1 = PHI * l2
    c = Point(width / 2.0, height / 2.0)
    angle = 0
    
    # Add 10 triangles in a star using a loop - one red, one blue per iteration
    for i in range(5):
        p1 = Point(width / 2.0 + l1 * cos(angle), height / 2.0 - l1 * sin(angle))
        angle += PI / 5.0
        p2 = Point(width / 2.0 + l2 * cos(angle), height / 2.0 - l2 * sin(angle))
        angle += PI / 5.0
        p3 = Point(width / 2.0 + l1 * cos(angle), height / 2.0 - l1 * sin(angle))
        tri.append(Type2(p2, c, p1))
        tri.append(Type2(p2, c, p3))
    return tri