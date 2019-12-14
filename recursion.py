def fibonacci(n):
    if n == 1 :
        return 1
    elif n==0 :
        return 0 
    else:  
        return fibonacci(n-1) + fibonacci(n-2)

#print(fibonacci(10))

def explore(map,i,j):
    map[i][j] = '*'
    size = 1
    neighbours = [(-1,0), (0,1),(0,-1),(1,0)]
    for di, dj in neighbours:
        if i+ di >= h or i +di < 0 or j + dj >= w or j + dj < 0:
            continue
        if  map[i + di][j + dj] == '#':
            size = size + explore(map,i+di, j+dj)
    return size 
        
    

f = open('map.txt', 'r')
h, w = f.readline().split()
h = int(h)
w = int(w)

map = []
for i in range(h):
    map.append(list(f.readline().strip()))
f.close()

numofislands = 0
x=[]
for i in range(h):
    for j in range(w):
        if map[i][j] == '#':
            numofislands = numofislands + 1
            island_size = explore(map,i,j)
            x.append(island_size)
print(numofislands)
print(x)





