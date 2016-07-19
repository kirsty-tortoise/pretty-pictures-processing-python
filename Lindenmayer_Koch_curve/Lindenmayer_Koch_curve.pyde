'''
A Lindenmayer process is a way to generate fractals using an instruction set and a string rewriting rule.

The instruction set gies instructions to move a "turtle" across the screen, drawing as it goes.
In this case:
    F move forwards
    + rotates clockwise
    - rotates anticlockwise

The string rewriting rule moves from one instruction set to the next. In this case, the rule is:
    F -> F-F++F-F
    All other letters stay the same
So, for example, F+ would go to F-F++F-F+

The Koch curve is created by starting with the instruction set F++F++F and repeatedly applying the string rewriting rules.
'''

def setup():
    # Sets up canvas, background and colour
    size(1000, 1000)
    background(0)
    stroke(255)
    
    # stage records the current instruction set
    # n is the current iteration number
    global stage, n
    stage = "F++F++F"
    n = 0

def Lprocess(seq, angle, n):
    # This carries out the instruction set in the sequence and uses these instructions to draw to the screen.
    
    # a is the current angle and step is the size of each step
    a = 0
    step = 600.0 / (3 ** n)
    
    # Start x and y coordinates close to the centre
    x = width/2 - 250
    y = height/2 + 250
    
    # Go through each instruction in the sequeucne
    for j in seq:
        
        # Move forward and draw in a line from the old position to the new position
        if j == "F":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        
        # rotate clockwise or anticlockwise by changing the angle
        elif j == "+":
            a += angle
        elif j == "-":
            a -= angle

def nextstage(stage):
    # Applies the string replacement rules to move from one string to the next
    # F -> F-F++F-F
    # Other characters stay the same
    new = ""
    for k in stage:
        if k == "F":
            new += "F-F++F-F"
        else:
            new += k
    return new

def draw():
    # This doesn't do anything, but it ensures the program runs and listens to clicks.
    pass

def mousePressed():
    # When you click the mouse, move to the next stage.
    # Transform the instruction set, add one to the iteration number, reset the background and carry out the instructions
    global stage, n
    stage = nextstage(stage)
    n += 1
    background(0)
    Lprocess(stage, 60, n)
    
