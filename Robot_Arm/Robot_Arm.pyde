def setup():
    size(700,500)
    background(255)
def draw():
    x=mouseX
    y=mouseY
    pushMatrix()
    background(255)
    strokeWeight(20)
    line(x,y,x+60,y+20)
    popMatrix()
    fill(0)
    ellipse(x,y,40,40)
