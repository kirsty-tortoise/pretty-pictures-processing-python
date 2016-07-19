'''
This image is generated using the Newton Raphson method to solve z^n = 1.
Each complex number is used as a starting point of the iteration, and is coloured
based on which root it converges to.
'''

# Solving the equation z^n = 1
# roots stores all the roots, working them out using de Moivres 
n = 2
roots = [complex(cos(TAU * i / n), sin(TAU * i / n)) for i in range(n)]
black = color(0)

def setup():
    # Sets up canvas, background and colours
    size(800, 800)
    background(black)
    colorMode(HSB, 100) # HSB used so I can cycle through the colours
    
    # cs is a list of the colours for each root
    global cs
    cs = [color(100.0 * i / n, 80, 100) for i in range(n)]

def draw():
    # Test 100 complex numbers each frame
    for j in range(100):
        z = 2
        
        # Choose a random complex number with an absolute value less than 2
        while abs(z) >= 2:
            z = complex(random(-2, 2), random(-2, 2))
            
        # points will collect all the points you pass when carrying out the iteration
        # They all converge to the same root, so can be coloured the same colour
        points = []
        
        # Checking says whether you have found a root yet
        Checking = True
        while Checking: 
            points.append(z)
            z = nextz(z)
            
            # If you find a root, set Checking to False and colour in all the points
            for j in range(n):
                if approxequal(z, roots[j]):
                    Checking = False
                    stroke(cs[j])
                    for i in points:
                        plot(i)
                        
def mouseClicked():
    # When clicked, increase n, and set roots and colours accordingly
    global n, roots, cs
    background(black)
    n += 1
    roots = [complex(cos(TAU * i / n), sin(TAU * i / n)) for i in range(n)]
    cs = [color(100.0 * i / n, 80, 100) for i in range(n)]
 
   
def nextz(z):
    # Carries out Newton Raphson method
    return z - (z ** n - 1) / (n * z ** (n - 1))

def plot(z):
    # Takes a complex number and plots it to the screen in the right place
    point((z.real + 1.5) * width / 3.0, height - (z.imag + 1.5) * height / 3.0)
    
def approxequal(z1, z2):
    # Checks if the number found is close to an actual root
    return abs(z1 - z2) < 10 ** -5
