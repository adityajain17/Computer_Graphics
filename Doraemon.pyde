def setup():
    size(800, 800, P3D)
    background(255)
    
def draw():
    with pushMatrix(): #blue sphere
        translate(400,200)
        noStroke()
        fill(0,191,255)
        pointLight(255,255,255,400,200,1000)
        sphere(100)
    with pushMatrix(): #big ellipse
        translate(400,248,100)
        stroke(0)
        fill(255)
        ellipse(0,0,150,130)
    with pushMatrix(): #left eye
        translate(385,180,110)
        stroke(0)
        fill(255)
        ellipse(0,0,30,40)
    with pushMatrix(): #right eye
        translate(415,180,110)
        stroke(0)
        fill(255)
        ellipse(0,0,30,40)
    with pushMatrix(): #inner left eye
        translate(390,190,110)
        noStroke()
        fill(0)
        ellipse(0,0,15,18)
        fill(255)
        strokeWeight(5)
        ellipse(2,5,7,9)#innner cornea
    with pushMatrix(): #inner right eye
        translate(410,190,110)
        noStroke()
        fill(0)
        ellipse(0,0,15,18)
        fill(255)
        strokeWeight(5)
        ellipse(-2,5,7,9)
    with pushMatrix(): #nose
       translate(400,210,100)
       stroke(0)
       noStroke()
       fill(255,0,0)
       sphere(12)
    with pushMatrix(): #black line
        translate(400,200,100)
        fill(0)
        stroke(0)
        line(0,0,0,50)
    with pushMatrix(): #whiskers
        translate(400,200,100)
        stroke(0)
        fill(0)
        line(30,15,65,0)#right 3 whiskers
        line(30,25,65,25)
        line(30,35,65,50)
        line(-30,15,-65,0)#left 3 whiskers
        line(-30,25,-65,25)
        line(-30,35,-65,50)
    with pushMatrix(): #full mouth(inner/outer tongue all included)
        translate(400,200,100)
        stroke(0)
        fill(0)
        line(0,0,0,50)
        translate(0,50,0)
        fill(255,0,0)
        arc(0,0,100,100,0,PI)
        fill(0)
        line(-50,0,50,0)
        fill(200,0,0)
        arc(0,50,80,60,5*PI/4-PI/6+radians(10),7*PI/4+PI/6-radians(10))
    with pushMatrix():
        strokeWeight(1)
        fill(255,0,0)
        bezier(335,270,275,320,525,320,465,270)
        translate(400,315)
        fill(255,235,59)
        noStroke()
        sphere(15)
