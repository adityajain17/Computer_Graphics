t1=3
t2=4
colorT=10
x=noise(t1)
y=noise(t2)
def setup():
    size(700,700)
    background(0)
def draw():
    global x,t1,t2,colorT,y
    background((noise(colorT)*100))
    x=noise(t1)
    y=noise(t2)
    colorT=colorT+0.01
    x=x*1000
    y=y*1000
    t1=t1+0.01
    t2=t2+0.01
    ellipse(x%width,y%height,30,30)
