'''
A Lindenmayer process is a way to generate fractals using an instruction set and a string rewriting rule.

The instruction set gies instructions to move a "turtle" across the screen, drawing as it goes.
In this case:
    A or B move forwards
    + rotates clockwise
    - rotates anticlockwise

The string rewriting rule moves from one instruction set to the next. In this case, the rule is:
    A -> +B-A-B+
    B -> -A+B+A-
    All other characters stay the same
So, for example, A+B would go to +B-A-B++-A+B+A-

The Sierpinski triangle fractal is created by starting with the instruction set A and repeatedly applying the string rewriting rules.
'''

def setup():
    # Sets up the canvas, background and colours
    size(1000, 1000)
    background(0)
    stroke(255)
 
    # stage stores the current instruction set, and n stores the number of iterations
    global stage, n
    stage = "A"
    n = 0

def Lprocess(seq, angle, n):
    # a is the current angle, and step is the step size
    a = 0
    step = 600.0 / (2 ** n)
    
    #x and y coordinates start near the middle
    x = width/2 - 300
    y = height/2 + 300
    
    # Go through each instruction in the instruction set
    for j in seq:
        # If A or B, then move forwards
        if j == "A" or j == "B":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        
        # If + or -, rotate the correct way
        elif j == "+":
            a += angle
        elif j == "-":
            a -= angle

def nextstage(stage):
    # This carries out the string rewriting rule to get from one stage to the next
    # A -> +B-A-B+
    # B -> -A+B+A-
    # All other characters stay the same
    new = ""
    for k in stage:
        if k == "A":
            new += "+B-A-B+"
        elif k == "B":
            new += "-A+B+A-"
        else:
            new += k
    return new

def draw():
    # Nothing happens here, but it means that the program runs in actual time and pressing the mouse works
    pass

def mousePressed():
    # When clicked, move to the next iteration.
    # Increase the iteration number by 1 and use the string rewriting rules to make the next instruction set 
    global stage, n
    stage = nextstage(stage)
    n += 1
    
    # Then reset the background and follow the instruction set
    background(0)
    Lprocess(stage, 60, n)
    