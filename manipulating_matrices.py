def matrix_fcn(n,m): #utility function; returns a n*m zero matrix
    matrix=[]
    for i in range (n):
        line = []
        matrix.append(line)
        for j in range (m):
            line.append('0')
    return matrix

my_matrix = [
    [ 5,  4,  6, -3],
    [ 4,  7, 10,  9],
    [12,  6, 11,  5],
    [ 2, -2,  1,  3],
    [ 1,  7, -1,  5],    
]

def extract_column(m, i):
    column = []
    for el in m:
        for j in el:
            if el.index(j) == i :
                column.append(el[el.index(j)])
    return column  

#print(extract_column(my_matrix, 2))

def modify_column(m, i, l):
    if len(l) > len(m): 
        while len(l) != len(m) :
            l.pop()
    
    if len(l) < len(m): 
       for el in m: 
            if m.index(el) > len(l)-1:
                l.append(el[i])
    if len(l) == len(m):
        while l != []:
            for el in m: 
                el[i] = l[0]
                l.pop(0)
    return m

#print(modify_column(my_matrix, 2, [2, -5, 6, 10, 11, 12]))

def sort_columns(m):
    for i in range(len(m)-1):
        v = extract_column(m,i)
        v.sort()
        new_m = modify_column(m, i, v)
    return new_m
#print (sort_columns(my_matrix))

def snake(n):
    mat = matrix_fcn(n, n)
    for i in range(1,n):
        for el in mat :
            for j in el: 
                if i % 2 == 1:
                    mat[i][el.index(j)] = (i-1)*n + 1 + el.index(j)
                else : 
                    mat[i][el.index(j)] = i*n - el.index(j)
    mat.pop(0)
    line = []
    for x in range(1,n+1):
        line.append(n*(n-1) + x)
    mat.append(line)
    return mat

print(snake(7))






