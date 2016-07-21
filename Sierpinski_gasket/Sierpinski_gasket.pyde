'''
This program draws a Sierpinski gasket, which is a fractal made up of triangles.

On each iteration, each triangle is replaced by four smaller triangles:
    
   ^        ^
  / \      /_\
 /   \  -> ^  ^
/_____\   /_\/_\

And the central triangle is removed.

Repeating this gives the Sierpinski Gasket.

When running the program, click to move to the next iteration.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # Define addition as averaging, for weird confusing code. :P
    def __add__(A, B):
        return Point((A.x + B.x)/2.0 , (A.y + B.y)/2.0)    
    
    def plot(self):
        point(self.x, self.y)

def setup():
    size(400, 400)
    
    # Space either side of the triangle
    border = 40.0
    
    background(0)
    noStroke()
    fill(200,255,200)
    
    # Make an initial triangle (a triangle is a list of three points).
    global triangles
    triangles = [[Point(border, height - 2 * border), Point(width - border, height - 2 * border), Point(width / 2.0, height - 2 * border - (width - 2 * border) * sin(radians(60)))]]
    draw_all_triangles()


def draw():
    pass

def mouseClicked():
    global triangles
    background(0)
    newtriangles = []
    for i in triangles:
        newtriangles += make_baby_triangles(i)
    triangles = newtriangles
    draw_all_triangles()
    

def draw_triangle(l):
    triangle(l[0].x, l[0].y, l[1].x, l[1].y, l[2].x, l[2].y)

def draw_all_triangles():
    for i in triangles:
        draw_triangle(i)
        
def make_baby_triangles(tri):
    a = tri[0]
    b = tri[1]
    c = tri[2]
    return [[a, a + b, a + c], [b, a + b, b + c], [c, a + c, b + c]] # Using averaging to find the new triangles makes the code short