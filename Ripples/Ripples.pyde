'''
This was some pretty picture stuff that I made when I was bored one day. 

Basically, a ripple is a circle, which spreads out and fades over time. When the ripple gets too big and too faded, it is deleted.

In this program, small ripples are released from your cursor, and then they grow and fade. 
You can move your mouse around to draw pretty patterns, yay! 
Dark and light blue ripples are released in blocks, so you get some dark and light concentric circles, if you keep your mouse still.
'''

class Ripple(object):
    def __init__(self, centreX, centreY, r, g, b, opacityStep, rippleStep, maxSize):
        self.centreX = centreX
        self.centreY = centreY
        self.rippleSize = 0   
        
        self.opacityStep = opacityStep
        self.rippleStep = rippleStep
        self.maxSize = maxSize # Indicates when ripple can be deleted.
                  
        # Set up colours, starting at maximum opacity
        self.opacity = 100
        self.r = r
        self.g = g
        self.b = b
    
    def spread(self):
        self.opacity -= self.opacityStep
        self.rippleSize += self.rippleStep
        
    def drawRipple(self):
        stroke(self.r, self.g, self.b, self.opacity)
        noFill()
        ellipse(self.centreX, self.centreY, 2 * self.rippleSize, 2 * self.rippleSize)

ripples = []
rippleCount = 0
rippleNumber = 0

def setup():
    size(750, 750)
    strokeWeight(2) # use thicker strokes for less spaced out ripples
        
def draw():
    background(0)
    
    global rippleNumber # Keeps count of blocks of ripples. Always mod 20.
    if rippleNumber < 10:
        # Dark blue ripple
        newRipple = Ripple(mouseX, mouseY, 54, 7, 242, 1, 2, 200)
    else:
        # Light blue ripple
        newRipple = Ripple(mouseX, mouseY, 40, 185, 247, 1, 2, 200)
    ripples.append(newRipple) 
      
    global rippleCount
    rippleCount += 1
    rippleNumber = (rippleNumber + 1) % 20
    
    i = 0 
    while i < rippleCount: # While loop makes deletion possible
        ripple = ripples[i]
        ripple.spread()
        ripple.drawRipple()
        if ripple.rippleSize > ripple.maxSize:
            # Delete  oversized ripples
            rippleCount -= 1
            del ripples[i]
        else:
            i += 1 # Only increase if a ripple isn't deleted.