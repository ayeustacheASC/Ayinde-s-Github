from Processing import *
window(400,400)
fill(46,0,24)
rect(0,0,50,50)
fill(40,0,160)
rect(50,0,50,50)
def doMousePressed():
    print('mousePressed at ' + str(mouseX()) + ',' + str(mouseY()) )
    
onMousePressed += doMousePressed
    if MouseX <= 50 or mouseY <= 50:
    fill(46,0,24)
if mouseC <= 100 or mouseY <= 100:
    fill(40,0,160)
def square
rect(
