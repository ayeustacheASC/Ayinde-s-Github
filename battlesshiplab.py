from Processing import*
from random import*

window(400,400)
grid = []
for i in range (0,5):
    for j in range (0,5):
        if j == 0:
            lst = [0]
        else:
            lst.append(0)
        rect(j*50,i*50,50,50)
    grid.append(lst)
 
idx1 = randrange(len(grid[0]))
idx2 = randrange(len(grid[0]))

grid[idx1][idx2] = 1

guess = 0
print (idx1,idx2)
while guess != (

while guess == False:
    if g
    
    
print (idx1,idx2)
print(grid)

