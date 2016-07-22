#set-up, ball, window, 4 walls
#make ball move in random direction 
#randrange()
#if the ball hits wall 
#then reverse direction
from Processing import*
def setup():
    window( 600, 600 )
    rect(20,10,550,550)
    blue = color(0,0,255)
    fill(blue)
  
setup()
i = 300

def moveRight():
    global i
    while i <= 570: 
        delay(2)
        background(255)
        rect(20,10,550,550)
        i = i + 1
   

def moveLeft():
    global i
    while i >= 25: 
        delay(2)
        background(255)
        rect(20,10,550,550)
        i = i - 1


while True:
    moveLeft()
    moveRight()

   
    


