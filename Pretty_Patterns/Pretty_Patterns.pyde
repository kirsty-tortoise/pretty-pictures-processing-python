'''
Here are some pretty patterns. I made them last year just before results day, so I was pretty stressed and needed distracting.

To get a new pattern press either:
    a - Nicely lined up hexagon patterns (with a few missing, for variety)
    b - Just some random hexagons with rotational symmetry

These are just some pretty patterns. There are type A and type B pretty patterns, but both are made of regular hexagons, and rotational symmetry of order 6 is enforced.

In type A patterns, the patter in made of a hexagonal lattice of random colours, with everything rotated to keep the symmetry.
In type B patterns, the hexagons are just put in a random position, again with rotating each rectangle for symmetry.

'''

def hexagon(centreX, centreY, radius):
    # Creates a hexagon about the centre, using magic creating a polygon stuff. 
    beginShape()
    for j in range(0, 360, 60):
        vertex(centreX + radius * cos(radians(j)), centreY + radius * sin(radians(j)))
    endShape(CLOSE)

def drawhexagons(radius):
    indent = 0 # Changes between "indented" and "unindented" columns in hexagonal lattice.
    for i in range(width / 8 , width - width / 8, radius):
        indent = not indent # Flip indent from 0 -> 1
        
        for j in range(height / 8, height - height / 8, int(2 * sqrt(3) * radius)):
            if random(1) > 0.35: # Draw 65% of the lattice hexagons, for variety
                fill(random(100), 50, 80, 40)
                
                # Draw 6 hexagons rotationally symmetrically
                for count in range(6):
                    hexagon(j + radius * sqrt(3) * indent, i, radius)
                    
                    # Translate to the origin, then rotate, then translate back to rotate about centre
                    translate(width / 2, height / 2)
                    rotate(PI/3.0)
                    translate(- width / 2,- height / 2)
                    
def drawrandomhexagons(radius):
    # Draw 40 random hexagons and rotations of each for symmetry.
    for x in range(40):
        i = random(0, width)
        j = random(0, height)
        fill(random(100), 50, 80, 50)
        
        # Draw 6 hexagons rotationally symmetrically.
        for count in range(6):
                hexagon(i, j, radius)
                
                # Translate to the origin, then rotate, then translate back to rotate about centre
                translate(width / 2, height / 2)
                rotate(PI/3.0)
                translate(- width / 2,- height / 2)

def setup():
    # Set up screen
    size(800, 800)
    noStroke()
    
    background(0)
    colorMode(HSB, 100) # HSB for nicer random colours
    drawrandomhexagons(40)
    
def draw():
    pass
    
def keyPressed():
    background(0) # Reset image
    if key == "a":
        drawhexagons(40)
    elif key == "b":
        drawrandomhexagons(40)
    