world_1 = [
    [False, False, False, False, False, False],
    [False, False, False, True, False, False],
    [False, True, False, False, True, False],
    [False, True, False, False, True, False],
    [False, False, True, False, False, False],
    [False, False, False, False, False, False]
     ]
 
world_2 = [
    [False, False, False, False],
    [False, True, True, False],
    [False, True, True, False],
    [False, False, False, False]
     ]
     
def alive(world, i, j):
    count = 0
    if world[i][j-1]== True :
        count += 1
    if world[i][j+1]==True:
        count+= 1
    if world[i-1][j]== True:
        count+=1
    if world[i+1][j] == True:
        count+=1
    if world [i-1][j-1] == True:
        count+=1
    if world[i-1][j+1]== True:
        count+=1
    if world[i+1][j-1] == True:
        count+=1
    if world[i+1][j+1] == True:
        count+=1
  
    return count

print(alive(world_1,2,0))

def game(world):
    for x in world:
        c = world.index(x)
        for y in x: 
            if world[c][y]== True :
                if alive(world, world[c], world[y]) < 2 or alive(world, world[c], world[y]) > 3 :
                    world[c][y]= False 
                else: 
                    pass 
            if world[c][y]== False:
                if alive(world, world[c], world[y]) == 3:
                    world[c][y]= True 
                else:
                    pass
    return world
print(game(world_1))

