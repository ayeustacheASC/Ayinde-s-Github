from Processing import*
window(400,400)
shipX=200
alienX= 50
def drawAlien():
    global alienX
    alienCount=0
    while alienCount<5:
        fill(255)
        rect(alienX,50,40,40)
        alienX+=65
        alienCount+=1
drawAlien()
    
def draw():
    background(0)
    global shipX
    noStroke()
    fill(255)
    ellipse(shipX,350,50,50)

def doKeyPressed():
    global shipX
    if key()== 'a':
        shipX -= 10
    elif key()=='d':
        shipX += 10
    draw()
onKeyPressed+=doKeyPressed
    
doKeyPressed()
