white = color(255)
black = color(0)

def draw_squares(x, y, a, b, scaled, square_num):
    strokeWeight(1)
    colorMode(HSB, 100)
    fill((square_num * 9 - 7) % 100, 80, 90)
    stroke(black)
    if a != 0 and b != 0:
        if square_num % 2 == 0:
            number_of_squares = b / a
        else:
            number_of_squares = a / b
        if square_num % 4 == 1:
            for count in range(number_of_squares):
                rect(x + count * b * scaled, y, b * scaled, b * scaled)
            draw_squares(x + b * scaled * number_of_squares, y, a % b, b, scaled, square_num + 1)
        elif square_num % 4 == 2:
            for count in range(number_of_squares):
                rect(x, y + count * a * scaled, a * scaled, a * scaled)
            draw_squares(x, y + a * scaled * number_of_squares, a, b % a, scaled, square_num + 1)
        elif square_num % 4 == 3:
            for count in range(number_of_squares):
                rect(x + scaled * (a - b - b * count), y, b * scaled, b * scaled)
            draw_squares(x, y, a % b, b, scaled, square_num + 1)
        elif square_num % 4 == 0:
            for count in range(number_of_squares):
                rect(x, y + scaled * (b - a - a * count), a * scaled, a * scaled)
            draw_squares(x, y, a, b % a, scaled, square_num + 1)
            
class button:
    def __init__(self, xcorner, ycorner, w, h, entry, colour = color(255)):
        self.xcorner = xcorner
        self.ycorner = ycorner
        self.w = w
        self.h = h
        self.entry = entry
        self.colour = colour
        
    def isOver(self):
        return self.xcorner <= mouseX <= self.xcorner + self.w and self.ycorner <= mouseY <= self.ycorner + self.h
    
    def drawButton(self):
        noStroke()
        fill(self.colour)
        rect(self.xcorner, self.ycorner, self.w, self.h, 10)
        textAlign(CENTER, CENTER)
        textSize(30)
        fill(0)
        text(" " + self.entry, self.xcorner, self.ycorner, self.w, self.h)

class inputBox(button):
    def __init__(self, xcorner, ycorner, w, h):
        self.xcorner = xcorner
        self.ycorner = ycorner
        self.w = w
        self.h = h
        self.entry = ""
        self.writing = False
    
    def drawButton(self):
        if self.writing:
            fill(100, 255, 100)
            stroke(white)
            strokeWeight(3)
        else:
            fill(200, 255, 200)
            noStroke()
        rect(self.xcorner, self.ycorner, self.w, self.h, 10)
        textAlign(LEFT, CENTER)
        textSize(40)
        fill(0)
        text(" " + self.entry, self.xcorner, self.ycorner, self.w, self.h)
        
    def getInput(self):
        if self.writing:
            if key == "":
                self.entry = self.entry[:-1]
            elif key in [str(i) for i in range(10)]:
                self.entry += str(key)
    
    def buttonPressed(self):
        if self.isOver():
            self.writing = True
            self.entry = ""
        else:
            self.writing = False
            
a = 29
b = 19

def setup():
    global a_box, b_box, update
    colorMode(HSB, 100)
    size(1000, 1000)
    background(0)
    a_box = inputBox(0.05 * width, 0.05 * height, 0.2 * width, 0.1 * height)
    b_box = inputBox(0.3 * width, 0.05 * height, 0.2 * width, 0.1 * height)
    update = button(0.6 * width, 0.05 * height, 0.3 * width, 0.1 * height, "UPDATE")
    draw_all()

def draw():
    pass

def mouseClicked():
    a_box.buttonPressed()
    b_box.buttonPressed()
    if update.isOver():
        global a, b
        a = int(a_box.entry)
        b = int(b_box.entry)
    draw_all()
        
def draw_all():
    background(black)
    a_box.drawButton()
    b_box.drawButton()
    update.drawButton()
    draw_squares(50, 250, a, b, min((width - 100.0) / a, (height - 300.0) / b), 1)

def keyPressed():
    a_box.getInput()
    b_box.getInput()
    a_box.drawButton()
    b_box.drawButton()
    update.drawButton()
