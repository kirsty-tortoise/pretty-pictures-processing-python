'''
The Koch curve is a fractal with the following replacement rules:

You start with a line, like this
--------------

On each iteration, you replace each line with four new lines, like this:
      /\
     /  \
----/    \----

In the Random Koch curve, you replace it with this half the time (at random) instead:
    
----\    /----
     \  /
      \/

This makes a more random, coastline-ish shape.

It uses an Lindenmayer process (or L process) to create the image.

A Lindenmayer process is a way to generate fractals using an instruction set and a string rewriting rule.

The instruction set gies instructions to move a "turtle" across the screen, drawing as it goes.
In this case:
    F move forwards
    + rotates anticlockwise
    - rotates clockwise

The string rewriting rule moves from one instruction set to the next. In this case, the rule is:
    F -> either F-F++F-F or F+F--F+F (chosen at random for each F)
    All other letters stay the same

The Koch curve is created by starting with the instruction set F and repeatedly applying the string rewriting rules.

When running the program, click to move to the next iteration.

'''

def setup():
    global stage, n
    size(1000, 1000)
    background(0)
    stroke(255)
    stage = "F" # Stores the sequence of instructions
    n = 0

def Lprocess(seq, angle, n):
    a = 0
    step = 600.0 / (3 ** n) # Scale step size depending on iteration number (each line decreases by a factor of 3 each time).
    
    # Always start in the centre.
    x = width/2 - 250
    y = height/2 + 250
    
    for j in seq:
        if j == "F": # Move forwards
            newx = x + step * cos(radians(a))
            newy = y - step * sin(radians(a))
            line(x, y, newx, newy)
            x, y = newx, newy
        elif j == "+": # Turn anticlockwise
            a += angle
        elif j == "-": # Turn clockwise
            a -= angle

def nextstage(stage):
    new = "" # New string to store instruction set
    for k in stage:
        num = random(1)
        if k == "F":
            if num >= 0.5:
                new += "F-F++F-F"
            else:
                new += "F+F--F+F"
        else:
            new += k
    return new

def draw():
    pass

def mousePressed():
    global stage, n
    
    # Advance to next stage, reset background and draw
    stage = nextstage(stage)
    n += 1
    background(0)
    Lprocess(stage, 60, n)