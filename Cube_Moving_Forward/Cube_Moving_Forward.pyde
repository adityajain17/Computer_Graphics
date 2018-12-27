x=list()
y=list()
z=list()
def setup():
    size(600,600,P3D)
    background(150)
    #frameRate(5)
    rand()
    
def draw():
    fill(255,0,0)
    global x,y,z
    background(150)
    for i in range(80):
        pushMatrix()
        translate(x[i],y[i],z[i])
        fill(random(25),random(25),random(255))
        box(20)
        popMatrix()
        z[i]=(z[i]+4)%400
    
def rand():
    global x,y,z
    x.remove
    for i in x:
        x.remove(i)
    for i in y:
        y.remove(i)
    for i  in range(80):
        x.append(random(400)+100)
        y.append(random(400)+100)
        z.append(random(50))
