'''
When you have a system of differential equations, you can have a point attractor. 
This is a point (x, y, z), which, if you start close enough and follow the differential equations, you will come towards this point.

However, you can also have an attractor that isn't just a point, but a set of points. That is what the Lorenz attractor is. 
It is also a really cool fractally shape, which is why it is here. 

As the differential equations have three dimensions, the Lorenz attractor is also a three dimensional object.
We are only plotting the x and y coordinates here, as I haven't done three dimensional stuff before.

The equations in the case are:
    
dx/dt = sigma * (y - x)
dy/dt = x * (rho - z) - y
dz/dt = x * y - beta * z

For some constants sigma, beta and rho. You can change the constants if you like.
'''

# These constants can be changed to give different curves
sigma = 10
beta = 8/3.0
rho = 28

dt = 0.001

x = 1
y = 1
z = 1

# Run the iteration a few times to get to the attractor
for i in range(1000):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * dt
    y += dy * dt
    z += dz * dt

def setup():
    # Set up the screen.
    size(400, 400)
    background(255)

def draw():
    # Update values using rule
    global x, y, z
    for i in range(100): # Run several times per frame
        dx = sigma * (y - x)
        dy = x * (rho - z) - y
        dz = x * y - beta * z
        x += dx * t
        y += dy * t
        z += dz * t
        # Plot a point
        point((x + 20) * width / 40.0,  (y + 20) * height / 40.0)