sigma = 10
beta = 8/3.0
rho = 28

t = 0.001

x = 1
y = 1
z = 1
for i in range(1000):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * t
    y += dy * t
    z += dz * t

def setup():
    size(400, 400)
    background(255)

def draw():
    global x, y, z
    for i in range(100):
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * t
        y += dy * t
        z += dz * t
        point((x + 20) * width / 40.0,  (y + 20) * height / 40.0)
