x=0
def setup():
    size(600,600)
    
def draw():
    global  x
    x=x+20
    R=random(255)
    G=random(255)
    B=random(255)
    background(255)
    pushMatrix()
    fill(255)
    translate(mouseX,mouseY)
    rotate(radians(x))
    fill(R,G,B)
    rect(-20,-20,40,40)
    popMatrix()
