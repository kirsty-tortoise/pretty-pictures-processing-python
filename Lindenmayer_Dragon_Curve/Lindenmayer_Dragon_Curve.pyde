'''
A Lindenmayer process is a way to generate fractals using an instruction set and a string rewriting rule.

The instruction set gies instructions to move a "turtle" across the screen, drawing as it goes.
In this case:
    F, X or Y - move forwards (these are different for the string rewriting rules)
    + rotates clockwise
    - rotates anticlockwise

The string rewriting rule moves from one instruction set to the next. In this case, the rule is:
    X -> X+YF+
    Y -> -FX-Y
    All other letters stay the same
So, for example, X+Y would go to X+YF+ + -FX-Y

The dragon curve is created by starting with the instruction set FX and repeatedly applying the string rewriting rules.
'''


def setup():
    # Sets up the canvas, background and colour
    size(600, 600)
    background(0)
    stroke(300, 150, 150)
    
    # stage is the instruction set so far
    # n is the iteration number
    global stage, n
    stage = "FX"
    n = 0

def Lprocess(seq, angle, n):
    # a is the current angle, so the shape starts slightly tipped
    a = - 45 * n
    
    # step is the step size, shrunk for higher iterations
    step = 150.0 / (2 ** (n/2.0))
    x = width/2 - 100
    y = height/2
    
    # Carry out the instructions for each instruction in the sequence
    for j in seq:
        # F, X and Y represent moving
        if j in ("F", "X", "Y"):
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
            

        elif j == "+":
            a += angle
            
        elif j == "-":
            a -= angle

def nextstage(stage):
    # Replacement rules are carried out to move from one instruction set to the next
    # X -> X+YF+
    # Y -> -FX-Y
    # All other letters stay the same
    new = ""
    for k in stage:
        if k == "X":
            new += "X+YF+"
        elif k== "Y":
            new += "-FX-Y"
        else:
            new += k
    return new

def draw():
    # Nothing happens here, but it means that the program detects when the mouse is pressed
    pass

def mousePressed():
    # When you click the mouse, move to the next stage.
    # Transform the instruction set, add one to the iteration number, reset the background and carry out the instructions
    global stage, n
    stage = nextstage(stage)
    n += 1
    background(0)
    Lprocess(stage, 90, n)
