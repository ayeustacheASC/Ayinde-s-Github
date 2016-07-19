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
    ellipse(300,300,60,60)
setup()
i = 300
while i <= 570: 
    delay(10)
    background(255)
    ellipse(i,300,60,60)
    i = i + 1
i = 570
while i >= 25: 
    delay(10)
    background(255)
    ellipse(i,300,60,60)
    i = i - 1