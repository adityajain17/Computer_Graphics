def setup():
    size(600,600,P3D)
    background(150)
def draw():
    pushMatrix()
    translate(300,300)
    fill(255,0,0)
    triangle(-200.0,0.0,200.0,0.0,0.0,-200.0)
    popMatrix()
    pushMatrix()
    translate(275,200)
    #sphere(50)
    popMatrix()
