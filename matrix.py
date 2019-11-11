def identity(n):
    matrix = []
    for i in range (n):
        line = []
        matrix.append(line)
        for j in range (n):
            if j == i:
                line.append(1)
            else:
                line.append(0)
    print(matrix)
identity(3)

def transpose(mat):
    trans = matrix_fcn(len(mat[0]), len(mat))
    for i in range (len(mat)):  
       for j in range (len(mat[i])):
            trans[j][i] = mat[i][j]
    print(trans)
transpose([[1, 2], [3, 4], [5,6]])