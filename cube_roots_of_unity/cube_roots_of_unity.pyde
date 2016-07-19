'''
This image is generated using the Newton Raphson method to solve z^3 = 1.
Each complex number is used as a starting point of the iteration, and is coloured
based on which root it converges to.
'''

# These are the three roots of the equation z^3 = 1
roots = [complex(1, 0), complex(-0.5, sqrt(3)/2.0), complex(-0.5, -sqrt(3)/2.0)]

# The colours red, green and blue correspond to the 3 roots.
c1 = color(255, 0, 0)
c2 = color(0, 255, 0)
c3 = color(0, 0, 255)


def setup():
    size(400, 400)
    background(0)

def draw():
    # Chooses 100 random points per frame.
    for j in range(100):
        
        # Choose a complex number with an absolute value less than 2, for symmetry reasons
        z = 2
        while abs(z) >= 2:
            z = complex(random(-2, 2), random(-2, 2))
        
        # points contains a list of complex numbers that will be coloured once we have found which root they go to
        # It picks up all the points the iteration visits
        points = []
        
        # Checking tells us when we have found a root
        Checking = True
        while Checking: 
            points.append(z)
            z = nextz(z)
            
            # Checks if it is close to any of the roots
            # If so, set Checking to False and plot all the points you have gathered
            if approxequal(z, roots[0]):
                Checking = False
                stroke(c1)
                for i in points:
                    plot(i)
            elif approxequal(z, roots[1]):
                Checking = False
                stroke(c2)
                for i in points:
                    plot(i)
            elif approxequal(z, roots[2]):
                Checking = False
                stroke(c3)
                for i in points:
                    plot(i)
    
def nextz(z):
    # Carries out Newton Raphson Iteration
    return z - (z ** 3 - 1) / (3 * z ** 2)

def plot(z):
    # Plots a complex number as if it is on an Argand diagram
    point((z.real + 1.5) * width / 3.0, height - (z.imag + 1.5) * height / 3.0)
    
def approxequal(z1, z2):
    # Checks if z1 is quite close to z2
    return abs(z1 - z2) < 10 ** -5
