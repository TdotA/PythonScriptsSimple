n0 = 0
n1 = 1
n = 0
s = 0
while n <= 4*10**6:
    n = n1 + n0 
    n0 = n1 
    n1 = n 
    if n % 2 == 0 :
        s = s+n
    else: 
        pass
print(s)


