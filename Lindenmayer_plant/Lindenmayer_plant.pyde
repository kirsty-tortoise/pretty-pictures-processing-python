'''
A Lindenmayer process is a way to generate fractals using an instruction set and a string rewriting rule.

The instruction set gies instructions to move a "turtle" across the screen, drawing as it goes.
In this case:
    F move forwards
    + rotates clockwise
    - rotates anticlockwise
    [ add current position and direction to the stack
    ] set current position and direction to the item on the top of the stack

The string rewriting rule moves from one instruction set to the next. In this case, the rule is:
    X -> F-[[X]+X]+F[+FX]-X
    F -> FF
    All other letters stay the same
So, for example, X+F would go to F-[[X]+X]+F[+FX]-X+FF

The plant fractal is created by starting with the instruction set X and repeatedly applying the string rewriting rules.
'''

# step is the size of each step forwards. It changes through the iterations.
step = 200.0

def setup():
    # Sets up the canvas, background and colours
    size(600, 600)
    background(0)
    stroke(150, 300, 150)
    
    # stage stores the current instruction set, and n stores the number of iterations    
    global stage, n
    stage = "X"
    n = 0

def Lprocess(seq, angle, n):
    a = 45
    x = 100
    y = height - 100
    
    # saved is the stack of positions saved.
    saved = []
    
    # Go through each instruction in the instruction set
    for j in seq:
        # If F, then move forwards
        if j == "F":
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        
        # If +, then rotate clockwise
        elif j == "+":
            a += angle
        
        # If -, then rotate anticlockwise
        elif j == "-":
            a -= angle
            
        # If [, then add to the end of the stack
        elif j == "[":
            saved.append((x, y, a))
            
        # If ], then take the last item from the stack and set positions
        elif j == "]":
            x, y, a = saved.pop()

def nextstage(stage):
    # This carries out the string rewriting rule to get from one stage to the next
    # X -> F-[[X]+X]+F[+FX]-X
    # F -> FF
    # All other letters stay the same
    new = ""
    for k in stage:
        if k == "X":
            new += "F-[[X]+X]+F[+FX]-X"
        elif k== "F":
            new += "FF"
        else:
            new += k
    return new

def draw():
    # Nothing happens here, but it means that the program runs in actual time and pressing the mouse works
    pass

def mousePressed():
    # When clicked, move to the next iteration.
    # Increase the iteration number by 1, half the step size and use the string rewriting rules to make the next instruction set 
    global stage, n, step
    step /= 2.0
    stage = nextstage(stage)
    n += 1
    
    # Then reset the background and follow the instruction set
    background(0)
    Lprocess(stage, 25, n)
