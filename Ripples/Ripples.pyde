class Ripple(object):
    def __init__(self, centreX, centreY, r, g, b, opacityStep, rippleStep, maxSize):
        self.centreX = centreX
        self.centreY = centreY
        self.rippleSize = 0   
        
        self.opacityStep = opacityStep
        self.rippleStep = rippleStep
        self.maxSize = maxSize
                  
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
    strokeWeight(2)
        
def draw():
    background(0)
    global rippleNumber
    if rippleNumber < 10:
        newRipple = Ripple(mouseX, mouseY, 54, 7, 242, 1, 2, 200)
    else:
        newRipple = Ripple(mouseX, mouseY, 40, 185, 247, 1, 2, 200)
    ripples.append(newRipple)    
    global rippleCount
    rippleCount += 1
    rippleNumber = (rippleNumber + 1) % 20
    
    i = 0
    while i < rippleCount:
        ripple = ripples[i]
        ripple.spread()
        ripple.drawRipple()
        if ripple.rippleSize > ripple.maxSize:
            rippleCount -= 1
            del ripples[i]
        else:
            i += 1