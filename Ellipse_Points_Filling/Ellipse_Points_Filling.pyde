rad=90
i=0
t=1
def setup():
    size(600,600)
    background(0)

def draw():
    global rad,i,t
    t=t*-1
    i=(i+2)
    if(i==90):
        rad=rad+12
        i=0
    x=rad*cos(radians(i))
    y=rad*sin(radians(i))
    fill(255)
    if(t==1):
        r=5
    else:
        r=8
    ellipse(x,y,r,r)
    frameRate(200)
