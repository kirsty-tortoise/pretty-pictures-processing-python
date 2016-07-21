'''
This program was based on some Christmas card patterns that Vicky Neale wrote about:
https://www.theguardian.com/science/alexs-adventures-in-numberland/2015/nov/26/solving-for-xmas-how-to-make-mathematical-christmas-cards

Technically the suggestion was sewing them, but you can make patterns more quickly with programming! These patterns are a bit snowflake-ish.

The idea is that if you make lots of slightly changing lines, then the envelope of these lines can form a nice curve. 
To see how this works, join up the corresponding numbers below:
    
8
7
6
5
4
3
2
1
 8 7 6 5 4 3 2 1
 
This program essentially does that, but several times at different angles to make a snowflake and with the two lines not necessarily being 90 degrees apart.

When running the program, click to get a new pattern of snowflakes.
'''

def snowflakes(x, y, flakeLength, flakes = 6, numberOfPoints = 6):
    # A flake here refers to one branch of the snowflake.
    
    lastFlake = [] # Last set of points along a flake.
    l = flakeLength / float(numberOfPoints) # Length between points
    angled = TWO_PI / flakes # Angle between flakes
    
    # Add points for first flake
    for p in range(1, numberOfPoints + 1):
        lastFlake.append((x + p * l, y))
        
    for a in range(0, flakes + 1):
        newFlake = []
        angle = a * angled
        for p in range(1, numberOfPoints + 1):
            # Use trig to find coordinates of next point on flake and add to list.
            newFlake.append((x + p * l * cos(angle), y - p * l * sin(angle)))
            
            # Draw line diagonally (-p is backwards indexing)
            line(newFlake[-1][0], newFlake[-1][1], lastFlake[-p][0], lastFlake[-p][1])
            
        # Draw in the branch
        line(x, y, x + cos(angle) * flakeLength, y - sin(angle) * flakeLength)
        lastFlake = newFlake

def tileSnowflakes():
    background(0)
    colorMode(HSB, 360, 360, 360) # HSB for nice random coluors
    jump = 0
    for count1 in range(10):
        for count2 in range(12):
            stroke(random(360), 300, 300) # Choose a random bright colour
            snowflakes((count1 + 0.5) * width / 10 + jump, (count2 + 0.5) * width * sqrt(3) / 20, 48, 6, 6)
            
            # Change the jump, so every other row is indented.
            if jump == 0:
                jump = width / 20.0
            else:
                jump = 0

def setup():
    size(1000, 1000)
    tileSnowflakes()


def draw():
    pass

def mouseClicked():
    tileSnowflakes()