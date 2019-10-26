import math 
n = int(input('Enter the number: '))
i = 2
while i <= n  :
    if (n % i) == 0 :
        print(str(n) + ' is not a prime, it is divisible by ' + str(i))
        break
    elif n % i != 0 and i == n-1:
        print(str(n) + ' is a prime!')
        break
    else :
        i+=1
    