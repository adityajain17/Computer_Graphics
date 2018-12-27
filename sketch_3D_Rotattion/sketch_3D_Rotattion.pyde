x=0
def setup():
    size(1000,1000,P3D)
def draw():
    background(255)
    global x
    x=x+5
    rotateY(radians(x))   
    translate(width/2-200,height/2-200)
    pushMatrix()
    translate(200,200)
    sphere(50)
    popMatrix()
