for i in range(1, 500):
    for j in range (1, 500):
        for k in range (1, 500):
            if j + i + k == 1000 and i**2 == j**2 + k**2:
                print(str(i) + ' ' + str(k) + ' ' + str(j) )
            else : 
                k+=1
        j+=1
    i+=1