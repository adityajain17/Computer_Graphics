x=600
y=280
speedy=0
def setup():
    size(600,600)
    background(255)
    
def  draw():
    background(255)
    fill(0)
    rect(0,300,600,300)
    fill(255,0,0)
    global x,y,speedy,flag
    if(y<180):
        speedy=-3
    y=y-speedy
    if(y>=280):
        speedy=0
    ellipse(20,y,40,40)
    rect(x,240,30,60)
    x=x-2
    if(x<0):
        x=600
        
def keyPressed():
    global y,speedy
    if(keyCode==UP):
        speedy=3
