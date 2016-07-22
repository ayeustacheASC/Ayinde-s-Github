#Ayinde Eustache and Dannon Thomas
from Processing import *
window(400,400)
x=200
def draw():
    background(255,255,255)
    rect(x,350,60,10)
    rect(50,50,30,30)
    fill(145,67,68)
    rect(100,50,30,30)
    rect(150,50,30,30)
    rect(200,50,30,30)
    rect(250,50,30,30)
    rect(300,50,30,30)    
    delay(10)
        
        
draw()
while True:
    global x
    bullety = 350
    if isKeyPressed()==True:
        if keyCode()=="Left":
            x=x-3
            draw()
        elif keyCode()=="Right":
            x=x+3
            draw()
            
        elif keyCode () == 'b':
            while bullety >0:
                background(255,255,255)
                rect(x,350,60,10)
                rect(50,50,30,30)
                fill(145,67,68)
                rect(100,50,30,30)
                rect(150,50,30,30)
                rect(200,50,30,30)
                rect(250,50,30,30)
                rect(300,50,30,30)  
                ellipse(x+30,bullety,10,10)
                bullety= bullety - 10
                delay(10)
                
       
           
    
         
            
    
    
        
        