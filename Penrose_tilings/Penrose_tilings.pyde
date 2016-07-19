PHI = (1 + sqrt(5)) / 2.0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __mul__(A, B):
        return Point(A.x + (PHI - 1) * (B.x - A.x), A.y + (PHI - 1) * (B.y - A.y))

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def draw_edges(self):
        stroke(0)
        line(self.p2.x, self.p2.y, self.p3.x, self.p3.y)
        line(self.p1.x, self.p1.y, self.p3.x, self.p3.y)

class Type1(Triangle):
    def draw_triangle(self):
        noStroke()
        fill(255, 0, 0)
        triangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)
    
    def split_triangle(self):
        new1 = self.p1 * self.p2
        new2 = self.p3 * self.p1
        t1 = Type1(self.p3, new1, new2)
        t2 = Type1(self.p3, new1, self.p2)
        t3 = Type2(new2, self.p1, new1)
        return [t1, t2, t3]

class Type2(Triangle):
    def draw_triangle(self):
        noStroke()
        fill(0, 0, 255)
        triangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y)
    
    def split_triangle(self):
        new = self.p2 * self.p3
        t1 = Type1(self.p2, self.p1, new)
        t2 = Type2(new, self.p3, self.p1)
        return [t1, t2]

def setup():
    global triangles
    size(800, 800)
    triangles = star()
    draw_all(triangles)

def draw():
    pass

def mouseClicked():
    global triangles
    triangles = update_all(triangles)
    draw_all(triangles)

def draw_all(triangles):
    background(255)
    for i in triangles:
        i.draw_triangle()
    for i in triangles:
        i.draw_edges()

def update_all(triangles):
    newtriangles = []
    for i in triangles:
        newtriangles += i.split_triangle()
    return newtriangles

def half_kite():
    l = 2/3.0 * width
    bottom = height / 4.0
    p1 = Point(1/6.0 * width, height - bottom)
    p2 = Point(5/6.0 * width, height - bottom)
    p3 = Point(1/6.0 * width + cos(radians(36)) * l, height - bottom - l * sin(radians(36)))
    return [Type1(p1, p2, p3)]

def half_dart():
    l = 2/3.0 * width
    bottom = height / 2.5
    p1 = Point(width / 2.0, height - bottom - l * tan(radians(36))/2.0) 
    p2 = Point(1/6.0 * width, height - bottom)
    p3 = Point(5/6.0 * width, height - bottom)
    return [Type2(p1, p2, p3)]
    
def sun():
    tri = []
    l = 1/3.0 * width
    c = Point(width / 2.0, height / 2.0)
    angle = 0
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
    tri = []
    l2 = 1/4.0 * width
    l1 = PHI * l2
    c = Point(width / 2.0, height / 2.0)
    angle = 0
    for i in range(5):
        p1 = Point(width / 2.0 + l1 * cos(angle), height / 2.0 - l1 * sin(angle))
        angle += PI / 5.0
        p2 = Point(width / 2.0 + l2 * cos(angle), height / 2.0 - l2 * sin(angle))
        angle += PI / 5.0
        p3 = Point(width / 2.0 + l1 * cos(angle), height / 2.0 - l1 * sin(angle))
        tri.append(Type2(p2, c, p1))
        tri.append(Type2(p2, c, p3))
    return tri
