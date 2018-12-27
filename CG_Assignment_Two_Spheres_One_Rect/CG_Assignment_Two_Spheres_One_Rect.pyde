x=0
speed=4.0
x1=300
y1=0
def setup():
    size(600,600,P3D)
    background(255)
def draw():
    global x
    x=x+5
    background(255)
    pushMatrix()
    fill(250,40,50)
    translate(150,250)
    rotate(radians(x%360)) 
    sphere(100)
    popMatrix()
    pushMatrix()
    fill(25,118,210)
    translate(450,250)
    rotate(radians(-x%360))
    sphere(100)
    popMatrix()
    move()
    display()
def move():
    global y1
    y1=(y1+4)%height
def display():
    fill(233,30,99)
    rect(x1,y1,20,40)
