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