def setup():
    size(600,600)
    background(255)
def draw():
    r=50.0
    pushMatrix()
    translate(300,300)
    i=0
    while(i<=6.28318):
        x=r*cos(i)
        y=r*sin(i)
        i=i+0.00001
        x1=r*cos(i)
        y1=r*sin(i)
        line(x,y,x1,y1)
    popMatrix()
